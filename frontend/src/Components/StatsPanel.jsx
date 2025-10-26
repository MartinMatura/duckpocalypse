import React, { useEffect, useState} from "react";


export default function StatsPanel({ stats, onSimulationEnd }) {
  const [liveStats, setLiveStats] = useState(stats || null);
  const [isRunning, setIsRunning] = useState(true);
  
  useEffect(() => {
    if (!isRunning) return;

    const interval = setInterval(async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/get-next-step/");
      if (!response.ok) throw new Error("Failed to fetch simulation step");

      const data = await response.json();
      setLiveStats(data);

      //simultaion reports completion
      if (data.is_done === 1) {
        setIsRunning(false);
        clearInterval(interval);
        if (onSimulationEnd) onSimulationEnd();
      }
    } catch (err) {
      console.error("Error fetching step:", err);
      setIsRunning(false);
      clearInterval(interval);
    }
  }, 1000);
  
  
  return () => clearInterval(interval);
}, [isRunning, onSimulationEnd]);

if (!liveStats) {
  return (
    <div className="flex flex-col items-center justify-center h-full text-gray-600">
      <p>Waiting for simulation data...</p>
    </div>
  );
}

//Destructure stats
const {number=20, 
  happiness=20, 
  food_supply=20, 
  intelligence=5, 
  strength=20, 
  tiles_claimed = 0,
  tiles_total = 400,
  } = liveStats;

  //Helper
  const progressWidth = (value) => `${Math.min(value, 100)}%`;

return (
      <div className="space-y-6 text-gray-800">
        <h2 className="text-4xl font-semibold">Stats: </h2>

        {/* Tile Progress */}
        <div className="space-y-2 text-2xl font-medium">
          <p>
            Tiles claimed:{" "}
            <span className="font-bold text-green-500">
              {tiles_claimed}
            </span>{" "}
            / {tiles_total}
          </p>
          <div className="w-full bg-gray-200 h-4 rounded-full overflow-hidden shadow-inner">
            <div
              className="bg-green-400 h-full transition-all duration-500"
              style={{ width: progressWidth((tiles_claimed / tiles_total)*100)}}
              />
          </div>
        </div>

      {/* Duck Stats */}
      <h2 className="text-2xl font-semibold mt-6">
        And more importantly, ducks:
      </h2>

        <div className="space-y-4">
          {[
            { label: "Number:", value: number, color: "bg-blue-400"},
            { label: "Happiness: ", value: happiness, color: "bg-yellow-400" },
            { label: "IQ", value: intelligence, color: "bg-purple-400"},
            { label: "Food Supply: ", value: food_supply, color: "bg-red-400" },
            { label: "Strength", value: strength, color: "bg-orange-400" },
          ].map((stat) => (
            <div key={stat.label}>
              <p className="text-lg font-medium">
                {stat.label}:{" "}
                <span className="font-bold">{stat.value}</span>
              </p>
            <div className="w-full bg-gray-200 h-3 rounded-full overflow-hidden shadow-inner">
              <div
                className={`${stat.color} h-full transition-all duration-500`}
                style={{ width: progressWidth(stat.value)}}
                />
            </div>
          </div>
          ))}
        </div>

        {!isRunning && (
          <div className="mt-6 text-center text-green-600 font-semibold">
            Simulation complete!
          </div>
        )}
      </div>
  );
}
