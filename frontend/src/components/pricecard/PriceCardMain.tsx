import { Loader2 } from 'lucide-react';
import type { Price } from './PriceCard';

type PriceCardMainPropsType = {
  loading: boolean;
  prices: Price[] | [];
};

export const PriceCardMain = ({ loading, prices }: PriceCardMainPropsType) => {
  return (
    <div className="overflow-x-auto rounded-lg p-4 bg-white border border-gray-200 shadow-sm">
      <table className="w-full">
        <thead className="text-gray-400 text-xs font-normal">
          <tr>
            <th className="text-left p-4">Grain Type</th>
            <th className="text-right p-4">Price</th>
          </tr>
        </thead>
        <tbody>
          {loading && (
            <tr>
              <td colSpan={2} className="text-center py-4">
                <Loader2 className="animate-spin w-5 h-5 mx-auto" />
              </td>
            </tr>
          )}
          {!loading && prices.length === 0 && (
            <tr>
              <td colSpan={2} className="text-center py-4 text-gray-500">
                No prices available
              </td>
            </tr>
          )}
          {prices.map((price) => (
            <tr
              key={price.grain_type}
              className="hover:bg-stone-200 transition-colors cursor-pointer"
            >
              <td className="text-left p-4 text-sm font-medium">{price.grain_type}</td>
              <td className="text-right p-4 text-sm font-medium">${price.price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
