import { useState } from "react";
import { ChatBoxHeader } from "./ChatBoxHeader";
import { ChatBoxMain } from "./ChatBoxMain";
import { ChatBoxFooter } from "./ChatBoxFooter";

export const ChatBox = () => {
  const [response, setResponse] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  return (
    <section className="p-10 flex flex-col gap-8">
      <ChatBoxHeader />

      <ChatBoxMain setResponse={setResponse} setLoading={setLoading} />

      <ChatBoxFooter loading={loading} response={response} />
    </section>
  );
};
