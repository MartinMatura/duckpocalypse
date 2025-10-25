export default function StrategiesPanel({ onStart }) {
  return (
    <div>
      <p>Choose your strategy!</p>
      <button
        className="bg-yellow-300 px-4 py-2 rounded mt-4"
        onClick={onStart}
      >
        Start Simulation
      </button>
    </div>
  );
}
