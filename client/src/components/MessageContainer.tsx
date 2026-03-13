import type { Message } from "../types/ChatBot";

interface MessageContainerProps {
  message: Message;
}

const MessageContainer = ({ message }: MessageContainerProps) => {
  return <div>{message.text}</div>;
};

export default MessageContainer;
