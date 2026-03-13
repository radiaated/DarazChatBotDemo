import {
  useContext,
  useState,
  type ChangeEvent,
  type SubmitEventHandler,
} from "react";
import ChatBotContext from "../context/ChatBotContext";
import MessageContainer from "../components/MessageContainer";

const ChatBotPage = () => {
  const [queryText, setQueryText] = useState<string>("");

  const chatBotCxt = useContext(ChatBotContext);

  const onSubmit: SubmitEventHandler<HTMLFormElement> = (event) => {
    event.preventDefault();
    chatBotCxt?.sendQuery(queryText);
    setQueryText("");
  };

  return (
    <div>
      <h2>Daraz Chat Bot</h2>
      <div id="chat-status">
        {chatBotCxt?.isConnected ? "Connected" : "Disconnected"}
      </div>
      <div id="chat-connection-message">{chatBotCxt?.chatbotWSMessage}</div>
      <div id="chat-message-container">
        {chatBotCxt?.messages.map((message, idx) => (
          <MessageContainer message={message} key={idx} />
        ))}
      </div>
      <div id="chat-form-container">
        <form onSubmit={onSubmit} method="POST">
          <div id="chat-input-container">
            <input
              type="text"
              name="querymessage"
              value={queryText}
              onChange={(event: ChangeEvent<HTMLInputElement>) =>
                setQueryText(event.target.value)
              }
              autoComplete="off"
            />
          </div>
          <div id="chat-submit-container">
            <button type="submit">Send</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ChatBotPage;
