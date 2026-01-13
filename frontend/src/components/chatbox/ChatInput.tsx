import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { ArrowRight } from 'lucide-react';
import z from 'zod';

const ChatMessageSchema = z.object({
  message: z.string().min(1, 'Message is required.'),
});

type ChatType = z.infer<typeof ChatMessageSchema>;

type ChatInputPropsType = {
  sendMessage: (message: string) => void;
};

export const ChatInput = ({ sendMessage }: ChatInputPropsType) => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<ChatType>({
    resolver: zodResolver(ChatMessageSchema),
    defaultValues: {
      message: '',
    },
  });

  const onSubmit = (data: ChatType) => {
    sendMessage(data.message);
    reset();
  };

  return (
    <div className="p-4 bg-white border border-gray-200 rounded-lg shadow-sm">
      <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-4">
        <label className="text-base font-medium" htmlFor="message">
          Ask whatever you want...
        </label>
        <textarea
          className="resize-none focus:outline-none"
          id="message"
          {...register('message')}
        />
        {errors.message && <span className="text-red-500">{errors.message.message}</span>}
        <button
          className="self-end cursor-pointer p-2 bg-indigo-800 size-fit rounded-lg text-white"
          type="submit"
        >
          <ArrowRight size={16} />
        </button>
      </form>
    </div>
  );
};
