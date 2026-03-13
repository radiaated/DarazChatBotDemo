import React, { createContext, useRef, useEffect, useState } from "react";
import type { Message } from "../types/ChatBot";

interface ChatBotContextType {
  isConnected: boolean;
  sendQuery: (query: string) => void;
  messages: Message[];
  isSending: boolean;
}

interface ChatBotContextProviderProps {
  children: React.ReactNode;
}

const ChatBotContext = createContext<ChatBotContextType | null>(null);

export const ChatBotContextProvider = ({
  children,
}: ChatBotContextProviderProps) => {
  const [isConnected, setIsConnected] = useState<boolean>(false);
  const [isSending, setIsSending] = useState<boolean>(false);
  const [messages, setMessages] = useState<Message[]>([
    {
      text: "Hello, welcome to Daraz customer service. How can we help you?",
      sentBy: "bot",
      dateSent: new Date(),
    },
  ]);

  const ws = useRef<WebSocket | null>(null);

  const addMessage = (newText: string, sentBy: "bot" | "customer") => {
    const message: Message = {
      text: newText,
      dateSent: new Date(),
      sentBy: sentBy,
    };

    setMessages((state) => {
      const ms_ = [...state, message];
      return ms_;
    });
  };

  const sendQuery = (query: string) => {
    if (ws.current) {
      ws.current.send(JSON.stringify({ query }));
      addMessage(query, "customer");
      setTimeout(() => {
        setIsSending(true);
      }, 300);
    }
  };

  const value = {
    isConnected,
    sendQuery,
    messages,
    isSending,
  };

  useEffect(() => {
    ws.current = new WebSocket(import.meta.env.VITE_WS_URL + "/chat/chat_bot/");

    ws.current.onopen = () => {
      setIsSending(false);
      setIsConnected(true);
    };
    ws.current.onclose = () => {
      setIsSending(false);
      setIsConnected(false);
    };
    ws.current.onerror = () => {
      setIsSending(false);
      setIsConnected(false);
    };
    ws.current.onmessage = (event) => {
      const res = event.data;
      const json = JSON.parse(res);
      setIsSending(false);
      addMessage(json.response, "bot");
    };
  }, []);

  return (
    <ChatBotContext.Provider value={value}>{children}</ChatBotContext.Provider>
  );
};

export default ChatBotContext;
