import React, { useState } from "react";

export default function StrategiesPanel({ onSelect, onStart, selected }) {
  const strategies = [
  { name: "POI first - random", value: "poi_first_random", desc: "Aims for closest POI, then random" },
  { name: "POI first - bfs", value: "poi_first_bfs", desc: "Aims for closest POI, then BFS" },
  { name: "Random", value: "random_choice", desc: "Randomly selects next square" },
  { name: "BFS", value: "breadth_first", desc: "Breadth-first search" },
  { name: "Pub First", value: "pub_first", desc: "Aims for pubs first" },
  { name: "Bread First", value: "bread_first", desc: "Aims for shops first" },
  { name: "Library First", value: "library_first", desc: "Aims for libraries first" },
  { name: "Gym First", value: "gym_first", desc: "Aims for gyms first" }
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
            onClick={() => onSelect(s.value)}
            className={`bg-yellow-200 hover:bg-yellow-300 border border-yellow-400 rounded-lg p-3 cursor-pointer shadow transition-transform hover:scale-105 ${
             selected === s.value
             ? "bg-yellow-400 border-yellow-600"
             : "bg-yellow-200 hover:bg-yellow-300 border-yellow-400"
            }`}
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

