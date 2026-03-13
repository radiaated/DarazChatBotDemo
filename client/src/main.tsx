import { createRoot } from "react-dom/client";
import ChatBotPage from "./page/ChatBotPage";
import { ChatBotContextProvider } from "./context/ChatBotContext";
import "./index.css";

createRoot(document.getElementById("root")!).render(
  <ChatBotContextProvider>
    <ChatBotPage />
  </ChatBotContextProvider>,
);
