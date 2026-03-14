import {
  useContext,
  useEffect,
  useRef,
  useState,
  type ChangeEvent,
  type SubmitEventHandler,
} from "react";
import ChatBotContext from "../context/ChatBotContext";
import MessageContainer from "../components/MessageContainer";
import DarazLogo from "../assets/img/daraz_logo.png";

const ChatBotPage = () => {
  const [queryText, setQueryText] = useState<string>("");

  const chatBotCxt = useContext(ChatBotContext);

  const chatMessageContainer = useRef<HTMLDivElement | null>(null);

  const onSubmit: SubmitEventHandler<HTMLFormElement> = (event) => {
    event.preventDefault();
    if (queryText.length !== 0) {
      chatBotCxt?.sendQuery(queryText);
      setQueryText("");
    }
  };

  const onEnterKeyDown = (event: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (event.key == "Enter" && !event.shiftKey) {
      event.preventDefault();
      event.currentTarget.form?.requestSubmit();
    }
  };

  useEffect(() => {
    if (
      chatBotCxt?.messages &&
      chatBotCxt?.messages.length > 1 &&
      chatMessageContainer.current
    ) {
      chatMessageContainer.current.scrollTo({
        top: chatMessageContainer.current.scrollHeight,
        behavior: "smooth",
      });
    }
  }, [chatBotCxt?.messages]);

  return (
    <div className="absolute top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%] w-100 h-[80vh] bg-[#eaeef2] overflow-clip rounded-3xl border border-gray-100 drop-shadow-xl">
      <div className="relative h-full">
        <div className="flex justify-center items-center gap-2 p-4 bg-white drop-shadow-lg">
          <div className="border border-primary p-[0.15em] rounded-full overflow-clip">
            <img
              src={DarazLogo}
              alt="Daraz logo"
              className="h-14 w-14 object-cover"
            />
          </div>
          <div>
            <div className="font-black text-primary text-xl">Daraz Bot</div>
            <div
              id="chat-status"
              className="text-[0.65rem] text-gray-500 tracking-wide"
            >
              {chatBotCxt?.isConnected ? (
                <>
                  <i className="fa-solid fa-circle text-green-500 text-[0.5rem] mr-1"></i>
                  Online
                </>
              ) : (
                <>
                  <i className="fa-solid fa-circle text-red-600 text-[0.5rem] mr-1"></i>
                  Offline
                </>
              )}
            </div>
          </div>
        </div>

        <div
          id="chat-message-container"
          className="flex flex-col gap-2 h-[78%] p-4 overflow-scroll"
          ref={chatMessageContainer}
        >
          {chatBotCxt?.messages.map((message, idx) => (
            <MessageContainer message={message} key={idx} />
          ))}
          {chatBotCxt?.isSending && (
            <div className="px-4 py-2 text-sm w-fit rounded-xl bg-gray-300 text-gray-700 animate-popup-left">
              <i className="fa-solid fa-spinner animate-spin"></i>
            </div>
          )}
        </div>
        <div
          id="chat-form-container"
          className="absolute bottom-[1.5em] left-0 w-full z-30 shadow-[0_-10px_20px_rgba(0,0,0,0.10)]"
        >
          <form
            onSubmit={onSubmit}
            method="POST"
            className="flex justify-between items-center relative"
          >
            <div id="chat-input-container" className="w-full">
              <textarea
                name="querymessage"
                onKeyDown={onEnterKeyDown}
                value={queryText}
                onChange={(event: ChangeEvent<HTMLTextAreaElement>) =>
                  setQueryText(event.target.value)
                }
                placeholder="Type your message here"
                rows={1}
                autoComplete="off"
                className="w-full px-4 py-2 resize-none bg-white text-gray-500 overflow-hidden outline-offset-1 focus:outline-1 focus:outline-primary/50"
              />
            </div>
            <div id="chat-submit-container" className="absolute right-2">
              <button
                type="submit"
                className="p-2 rotate-45 text-gray-400 text-center cursor-pointer rounded-full hover:bg-primary hover:text-white"
              >
                <i className="fa-solid fa-paper-plane"></i>
              </button>
            </div>
          </form>
        </div>
        <div className="flex gap-1 justify-center w-full bg-[#f7f7f8] text-gray-600 text-xs text-center p-2 absolute bottom-0 left-0">
          <div>Powered by AI |</div>
          <a
            href="https://github.com/radiaated/DarazChatBotDemo"
            target="_blank"
            className="block font-black text-blue-700 hover:text-blue-900 duration-100"
          >
            Github <i className="fa-brands fa-github"></i>
          </a>
        </div>
      </div>
    </div>
  );
};

export default ChatBotPage;
