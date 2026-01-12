import { Loader2 } from "lucide-react";

type ChatBoxFooterPropsType = {
  loading: boolean;
  response: string;
};

export const ChatBoxFooter = ({
  loading,
  response,
}: ChatBoxFooterPropsType) => {
  return (
    <div className="flex items-center gap-2">
      {loading && <Loader2 className="animate-spin w-5 h-5" />}
      <p>{response}</p>
    </div>
  );
};
