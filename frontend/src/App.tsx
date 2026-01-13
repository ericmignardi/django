import { ChatBox } from './components/chatbox/ChatBox';
import { PriceCard } from './components/pricecard/PriceCard';

export const App = () => {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 p-10 min-h-screen">
      <PriceCard />
      <ChatBox />
    </div>
  );
};
