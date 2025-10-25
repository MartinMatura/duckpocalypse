import React from "react";

export default function SimulationArea() {
  return (
    console.log("SimulationArea is rendering"),
    <div className="flex justify-center items-center w-full h-full bg-green-100">
      <div className="grid grid-cols-10 grid-rows-10 gap-1 w-[80vmin] h-[80vmin] border border-green-500">
        {Array.from({ length: 100 }).map((_, i) => (
          <div
            key={i}
            className="bg-green-300 border border-green-500 aspect-square hover:bg-green-300 rounded-lg p-3 cursor-pointer shadow transition-transform hover:scale-105"
          ></div>
        ))}
      </div>
    </div>
  );
}

