import React from "react";


export default function StatsPanel() {
  return (
      <div className="space-y-6 text-gray-800">
        <h2 className="text-4xl font-semibold">Stats: </h2>

        <div className="text-2xl font-medium">
          <p>Tiles claimed: <span className="font-bold text-green-400">0</span></p>
          <p>Tiles left to conquer: <span className="font-bold text-red-400">400</span></p>
        </div>

        <h2 className="text-2xl font-semibold">And more importantly, ducks: </h2>

        <div className="text-2xl font-medium">
          <p>Number: <span className="font-bold text-blue-400">20</span></p>
          <p>Happiness: <span className="font-bold text-blue-400">20</span></p>
          <p>IQ: <span className="font-bold text-blue-400">20</span></p>
          <p>Hunger: <span className="font-bold text-blue-400">10</span></p>
          <p>Strength: <span className="font-bold text-blue-400">20</span></p>
        </div>
      </div>
  );
}
