import { ChatBox } from "./components/ChatBox";
import { PriceCard } from "./components/PriceCard";

export const App = () => {
  return (
    <div className="flex flex-col lg:flex-row justify-center items-center min-h-screen">
      <PriceCard />
      <ChatBox />
    </div>
  );
};
