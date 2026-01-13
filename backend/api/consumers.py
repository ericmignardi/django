import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import ChatMessage
from .chain import get_response


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat_history = []

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get('message', '')

            # Add user message to history
            self.chat_history.append({'role': 'user', 'content': message})

            # Call LangChain (wrapped for async)
            response_text = await self.get_ai_response(message)

            # Add assistant response to history
            self.chat_history.append({'role': 'assistant', 'content': response_text})

            # Save to database
            await self.save_message(message, 'user')
            await self.save_message(response_text, 'assistant')

            # Send response back to client
            await self.send(text_data=json.dumps({
                'type': 'chat_response',
                'text': response_text
            }))

        except Exception as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e)
            }))

    @sync_to_async
    def get_ai_response(self, message: str) -> str:
        """Get response from LangChain with chat history context."""
        return get_response(message, self.chat_history[:-1])  # Exclude the just-added user message

    @sync_to_async
    def save_message(self, content: str, role: str):
        ChatMessage.objects.create(role=role, content=content)


    # ============================================================
    # STREAMING VERSION (commented out for future implementation)
    # ============================================================
    # async def get_ai_response_stream(self, message: str):
    #     """
    #     Generator that yields text chunks as they come from Gemini.
    #     Note: Streaming doesn't support JSON schema, so you'd get raw text.
    #     """
    #     @sync_to_async
    #     def _stream():
    #         chunks = []
    #         for chunk in client.models.generate_content_stream(
    #             model='gemini-2.5-flash',
    #             contents=message,
    #         ):
    #             chunks.append(chunk.text)
    #             yield chunk.text
    #         # Save complete message after streaming
    #         full_response = ''.join(chunks)
    #         ChatMessage.objects.create(role='assistant', content=full_response)
    #
    #     async for chunk in _stream():
    #         yield chunk
    # ============================================================