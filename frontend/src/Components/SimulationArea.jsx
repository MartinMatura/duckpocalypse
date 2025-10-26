import React, { useEffect, useState } from "react";

export default function SimulationArea() {
  const [grid, setGrid] = useState(Array(20).fill().map(() => Array(20).fill({ owner: null })));

  // Fetch grid from FastAPI
  useEffect(() => {
    fetch("http://127.0.0.1:8000/grid/")
      .then((res) => res.json())
      .then((data) => setGrid(data.grid))
      .catch((err) => console.error("Error fetching grid:", err));
  }, []);

  return (
    <div className="flex justify-center items-center w-full h-full bg-green-100">
      <div className="grid [grid-template-columns:repeat(20,1fr)] [grid-template-rows:repeat(20,1fr)] gap-1 w-[80vmin] h-[80vmin] border border-green-500">
        {grid.map((row, i) =>
          row.map((cell, j) => (
            <div
              key={`${i}-${j}`}
              className={`aspect-square rounded-lg border border-green-500 transition-transform hover:scale-105 ${
                cell.owner === "duck"
                  ? "bg-yellow-400" // claimed by duck
                  : "bg-green-300 hover:bg-green-400" // unclaimed
              }`}
            ></div>
          ))
        )}
      </div>
    </div>
  );
}

