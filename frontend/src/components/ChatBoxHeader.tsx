export const ChatBoxHeader = () => {
  return (
    <header className="flex flex-col gap-2">
      <h1 className="text-5xl font-bold">
        <span className="bg-linear-to-r from-stone-950 via-indigo-800 to-blue-800 bg-clip-text text-transparent">
          Hi there, John
        </span>
        <br />
        <span className="bg-linear-to-r from-stone-950 via-indigo-800 to-blue-800 bg-clip-text text-transparent">
          What would you like to know?
        </span>
      </h1>
      <p className="text-lg leading-tight text-gray-500 max-w-sm">
        Use one of the most common prompts below or use your own to begin.
      </p>
    </header>
  );
};
