import { ChatBoxHeader } from './ChatBoxHeader';
import { ChatInput } from './ChatInput';
import { ChatMessages } from './ChatMessages';
import { useWebSocket } from '../../hooks/useWebSocket';

export const ChatBox = () => {
  const { messages, loading, sendMessage } = useWebSocket();

  return (
    <section className="p-10 flex flex-col gap-8">
      <ChatBoxHeader />
      <ChatMessages loading={loading} messages={messages} />
      <ChatInput sendMessage={sendMessage} />
    </section>
  );
};
