import React from "react";

export default function SimulationArea() {
  return (
    <div className="flex justify-center items-center w-full h-full bg-green-100">
      <div className="grid [grid-template-columns:repeat(20,1fr)] [grid-template-rows:repeat(20,1fr)] gap-1 w-[80vmin] h-[80vmin] border border-green-500">
        {Array.from({ length: 400 }).map((_, i) => (
          <div
            key={i}
            className="bg-green-300 border border-green-500 aspect-square hover:bg-green-400 rounded-lg cursor-pointer shadow transition-transform hover:scale-105"
          ></div>
        ))}
      </div>
    </div>
  );
}

