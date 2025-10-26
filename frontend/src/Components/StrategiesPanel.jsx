export default function StrategiesPanel({ onStart }) {
  const strategies = [
    { name: "POI first - random", desc: "Aims for closest point of interest, then random once all discovered" },
    { name: "POI first - bfs", desc: "Aims for closest point of interest, then uses a bfs algoritm once all discovered" },
    { name: "Random", desc: "Randomly selects next sqaure from its neighbours" },
    { name: "BFS", desc: "Breadth first search, all closest nodes, then all their closest nodes" },
    { name: "Pub First", desc: "Aims for pub points of interest first, then random once all discovered" },
    { name: "Bread First", desc: "Aims for shop points of interest first, then random once all discovered" },
    { name: "Library First", desc: "Aims for library points of interest first, then random once all discovered" },
    { name: "Gym First", desc: "Aims for gym points of interest first, then random once all discovered" }
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

