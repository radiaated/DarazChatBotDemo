import type { Message } from "../types/ChatBot";
import TimeAgo from "javascript-time-ago";
import en from "javascript-time-ago/locale/en";
import Markdown from "react-markdown";

TimeAgo.addDefaultLocale(en);

const timeAgo = new TimeAgo("en-US");

interface MessageContainerProps {
  message: Message;
}

const MessageContainer = ({ message }: MessageContainerProps) => {
  return (
    <div
      className={`w-full flex items-end gap-1 ${
        message.sentBy === "customer"
          ? "flex-row-reverse animate-popup-right"
          : ""
      } animate-popup-left`}
    >
      <div
        className={`flex flex-col gap-1.5 p-4 text-sm w-75 rounded-xl ${message.sentBy == "bot" ? "bg-primary text-white" : "bg-white text-gray-700"}`}
      >
        {message.text.split("\n").map((paragraph, idx) => (
          <Markdown key={idx}>{paragraph}</Markdown>
        ))}
      </div>
      <div className="text-[0.65rem] tracking-wide text-gray-500">
        {timeAgo.format(message.dateSent, "mini")}
      </div>
    </div>
  );
};

export default MessageContainer;
