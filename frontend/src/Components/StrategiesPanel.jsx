export default function StrategiesPanel({ onStart }) {
  const strategies = [
    { name: "Aggressive Ducks", desc: "Attack anything that moves." },
    { name: "Defensive Ducks", desc: "Hold formation and protect their pond." },
    { name: "Random Ducks", desc: "Chaos reigns supreme." },
    { name: "Smart Ducks", desc: "Adapt to survive." },
  ];

  return (
    <div className="flex flex-col h-full">
      <h2 className="text-2xl font-bold text-center mb-4 text-gray-700">
        Choose Your Strategy
      </h2>

      {/* Strategy grid */}
      <div className="grid grid-cols-2 gap-4 flex-grow">
        {strategies.map((s, i) => (
          <div
            key={i}
            className="bg-yellow-200 hover:bg-yellow-300 border border-yellow-400 rounded-lg p-3 cursor-pointer shadow transition-transform hover:scale-105"
          >
            <h3 className="font-semibold text-lg mb-1 text-gray-800">{s.name}</h3>
            <p className="text-sm text-gray-600">{s.desc}</p>
          </div>
        ))}
      </div>

      {/* Start button */}
      <button
        onClick={onStart}
        className="mt-6 bg-green-400 hover:bg-green-500 text-black font-bold py-3 px-6 rounded-lg shadow-lg transition-colors"
      >
        Start Simulation
      </button>
    </div>
  );
}

