import React, { createContext, useRef, useEffect, useState } from "react";
import type { Message } from "../types/ChatBot";

interface ChatBotContextType {
  isConnected: boolean;
  chatbotWSMessage: string | null;
  sendQuery: (query: string) => void;
  messages: Message[];
}

interface ChatBotContextProviderProps {
  children: React.ReactNode;
}

const ChatBotContext = createContext<ChatBotContextType | null>(null);

export const ChatBotContextProvider = ({
  children,
}: ChatBotContextProviderProps) => {
  const [isConnected, setIsConnected] = useState<boolean>(false);
  const [chatbotWSMessage, setchatbotWSMessage] = useState<string | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);

  const ws = useRef<WebSocket | null>(null);

  const addMessage = (newText: string) => {
    const message: Message = {
      text: newText,
      dateSent: new Date(),
    };

    setMessages((state) => {
      const ms_ = [...state, message];
      return ms_;
    });
  };

  const sendQuery = (query: string) => {
    if (ws.current) {
      ws.current.send(JSON.stringify({ query }));
      addMessage(query);
    }
  };

  const value = {
    isConnected,
    chatbotWSMessage,
    sendQuery,
    messages,
  };

  useEffect(() => {
    ws.current = new WebSocket(import.meta.env.VITE_WS_URL + "/chat/chat_bot/");

    ws.current.onopen = () => {
      setIsConnected(true);
      setchatbotWSMessage(null);
    };
    ws.current.onclose = () => {
      setIsConnected(false);
      setchatbotWSMessage(null);
    };
    ws.current.onerror = () => {
      setIsConnected(false);
      setchatbotWSMessage("Disconnected because of some error.");
    };
    ws.current.onmessage = (event) => {
      const res = event.data;
      const json = JSON.parse(res);
      addMessage(json.response);
    };
  }, []);

  return (
    <ChatBotContext.Provider value={value}>{children}</ChatBotContext.Provider>
  );
};

export default ChatBotContext;
