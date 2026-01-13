"""
LangChain integration for grain marketing AI assistant.

This module provides a conversational AI chain using LangChain with Google Gemini.
It includes a system prompt tailored for grain marketing advice.
"""
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

# Initialize the Gemini model via LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

# System prompt tailored for grain marketing (aligns with GrainFox's domain)
SYSTEM_PROMPT = """You are a knowledgeable grain marketing advisor. Your role is to help farmers and grain producers make informed decisions about:

- Current grain market conditions and price trends
- Optimal timing for selling grain
- Risk management strategies
- Market analysis and forecasting

Be concise, practical, and data-driven in your responses. If you don't have specific current market data, provide general guidance and recommend checking current prices.

Always be helpful and professional."""

# Create the prompt template with chat history support
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}")
])

# Create the chain: prompt -> LLM -> string output
chain = prompt | llm | StrOutputParser()


def get_response(message: str, chat_history: list = None) -> str:
    """
    Get an AI response using the LangChain chain.
    
    Args:
        message: The user's input message
        chat_history: Optional list of previous messages for context
        
    Returns:
        The AI's response as a string
    """
    history = []
    if chat_history:
        for msg in chat_history:
            if msg.get('role') == 'user':
                history.append(HumanMessage(content=msg.get('content', '')))
            elif msg.get('role') == 'assistant':
                history.append(AIMessage(content=msg.get('content', '')))
    
    return chain.invoke({
        "input": message,
        "chat_history": history
    })
