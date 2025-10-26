import React, { useEffect, useState } from "react";
import "./SimulationArea.css";

const duckMap = "/bg_poi_no_grid.png"

export default function SimulationArea() {
  const [grid, setGrid] = useState(Array(20).fill().map(() => Array(20).fill({ owner: null })));

  // Fetch grid from FastAPI
  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://127.0.0.1:8000/grid/")
        .then((res) => res.json())
        .then((data) => setGrid(data.grid))
        .catch((err) => console.error("Error fetching grid:", err));
    }, 1000); // update every second

    return () => clearInterval(interval);
  }, []);


  return (
    <div className="flex justify-center items-center w-full h-full bg-green-100">
      <div className="relative w-[80vmin] aspect-square">
       <img
          src={duckMap}
          alt="Duck map"
          className="absolute inset-0 w-full h-full object-cover opacity-80 rounded-lg"
        />


      {/*Transparent map overlay */}
      <div className="absolute inset-0 grid [grid-template-columns:repeat(20,1fr)] [grid-template-rows:repeat(20,1fr)] gap-[1px]">
        {grid.map((row, i) =>
          row.map((cell, j) => (
            <div
              key={`${i}-${j}`}
              className={`aspect-square rounded-lg border border-green-500 transition-transform hover:scale-105 ${
                cell.owner === "duck"
                  ? "bg-yellow-400/40 animate-pulse" // claimed by duck
                  : "bg-transparent hover:bg-green-300/40" // unclaimed
              }`}
            ></div>
          ))
        )}
      </div>
    </div>
  </div>
  );
}


