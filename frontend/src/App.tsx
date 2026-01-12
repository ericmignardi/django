import { ChatBox } from "./components/ChatBox";
import { PriceCard } from "./components/PriceCard";

export const App = () => {
  return (
    <div className="flex justify-center items-center min-h-screen">
      <PriceCard />
      <ChatBox />
    </div>
  );
};
