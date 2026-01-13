import { Loader2 } from 'lucide-react';
import type { ChatMessage } from '../../hooks/useWebSocket';

type ChatMessagesPropsType = {
  loading: boolean;
  messages: ChatMessage[];
};

export const ChatMessages = ({ loading, messages }: ChatMessagesPropsType) => {
  return (
    <div className="flex flex-col gap-4 max-h-96 overflow-y-auto">
      {messages.map((msg, index) => (
        <div
          key={index}
          className={`p-3 rounded-lg max-w-[80%] ${
            msg.role === 'user'
              ? 'bg-indigo-800 text-white self-end'
              : 'bg-gray-100 text-gray-800 self-start'
          }`}
        >
          <p className="text-sm font-medium mb-1">{msg.role === 'user' ? 'You' : 'AI'}</p>
          <p>{msg.content}</p>
        </div>
      ))}
      {loading && (
        <div className="flex items-center gap-2 text-gray-500">
          <Loader2 className="animate-spin w-5 h-5" />
          <span>Thinking...</span>
        </div>
      )}
    </div>
  );
};
