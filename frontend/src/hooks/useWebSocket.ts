import { useState, useEffect, useCallback, useRef } from 'react';

type WebSocketMessage = {
  type: 'chat_response' | 'error';
  text?: string;
  message?: string;
};

export type ChatMessage = {
  role: 'user' | 'assistant';
  content: string;
};

export const useWebSocket = () => {
  const [isConnected, setIsConnected] = useState(false);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const wsRef = useRef<WebSocket | null>(null);

  const wsUrl = import.meta.env.VITE_WS_URL || 'ws://localhost:8000/ws/chat';

  useEffect(() => {
    const connect = () => {
      const ws = new WebSocket(wsUrl);

      ws.onopen = () => {
        setIsConnected(true);
        setError(null);
      };

      ws.onclose = () => {
        setIsConnected(false);
        // Reconnect after 3 seconds
        setTimeout(connect, 3000);
      };

      ws.onerror = () => {
        setError('WebSocket connection error');
      };

      ws.onmessage = (event) => {
        const data: WebSocketMessage = JSON.parse(event.data);
        setLoading(false);

        if (data.type === 'chat_response') {
          setMessages((prev) => [...prev, { role: 'assistant', content: data.text || '' }]);
        } else if (data.type === 'error') {
          setError(data.message || 'Unknown error');
        }
      };

      wsRef.current = ws;
    };

    connect();

    return () => {
      wsRef.current?.close();
    };
  }, [wsUrl]);

  const sendMessage = useCallback((message: string) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      // Add user message to the list
      setMessages((prev) => [...prev, { role: 'user', content: message }]);
      setLoading(true);
      setError(null);
      wsRef.current.send(JSON.stringify({ message }));
    }
  }, []);

  return { isConnected, messages, loading, error, sendMessage };
};
