import { useEffect, useState } from "react";
import toast from "react-hot-toast";
import { axiosInstance } from "../api/axios";
import { PriceCardHeader } from "./PriceCardHeader";
import { PriceCardMain } from "./PriceCardMain";

export interface Price {
  grain_type: string;
  price: number;
}

export const PriceCard = () => {
  const [loading, setLoading] = useState<boolean>(false);
  const [prices, setPrices] = useState<Price[]>([]);

  useEffect(() => {
    const fetchPrices = async () => {
      setLoading(true);
      try {
        const response = await axiosInstance.get("/prices");
        if (response.status === 200) {
          setPrices(response.data);
          toast.success("Successfully read prices");
        } else {
          setPrices([]);
          toast.error("Unable to read prices");
        }
      } catch (error) {
        if (error instanceof Error ? error.message : "Error reading prices")
          toast.error("Error reading prices");
      } finally {
        setLoading(false);
      }
    };

    fetchPrices();
  }, []);

  return (
    <section className="p-10 flex flex-col gap-8">
      <PriceCardHeader />

      <PriceCardMain loading={loading} prices={prices} />
    </section>
  );
};
