import "./DuckSimulator.css"
import React, { useState } from "react";
import Header from "./Components/Header";
import SimulationArea from "./Components/SimulationArea";
import StatsPanel from "./Components/StatsPanel";
import StrategiesPanel from "./Components/StrategiesPanel";


export default function DuckSimulator() {
  const [simulationStarted, setSimulationStarted] = useState(false);
  const [selectedStrategy, setSelectedStrategy] = useState(null);
  const [stats, setStats] = useState(null);

  //start simulation using API
  const handleStart = async () => {
    if (!selectedStrategy) {
      alert("Please select a strategy first, quack!");
      return;
    }

  const payload = {
  happiness: 20,
  food_supply: 20,
  intelligence: 5,
  strength: 20,
  strategy: selectedStrategy,
  starting_x: 0,
  starting_y: 0,
};


  console.log("🦆 Sending start payload:", payload);

  try {
    const response = await fetch("http://127.0.0.1:8000/start-conditions/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
      
      if  (!response.ok) throw new Error("Failed to start simulation: $(text");

      const data = await response.json();
      console.log("Simulation started:", data);
      setStats(data);
      setSimulationStarted(true);
    } catch (error) {
      console.error("Error starting simulation:", error);
      alert("Could not start simulation.  Check FastAPI server status.");
    }
  };
  

  return (
    <div className="flex flex-col h-screen bg-[#fefae0]">
      <Header /> 

      <div className="flex flex-1 min-h-0 overflow-hidden h-full">
          {/* Map/Simulation Area on the left */}
          <div className="flex-grow h-full min-h-0 border-r border-gray-300 flex justify-center items-center">
            <SimulationArea isRunning={simulationStarted} />
          </div>

          {/*Right side stats or strategies panel --> one at a time*/}
          <div className="w-96 bg-[#fff9c4] border border-yellow-300 p-4 h-full overflow-y-auto">
          {!simulationStarted ? (
            <StrategiesPanel 
              selected={selectedStrategy}
              onSelect={setSelectedStrategy}
              onStart={handleStart} />
          ) : (
              <StatsPanel stats={stats} />
          )}
        </div>
      </div> 

      {/* Footer */}
      <footer className="fixed bottom-2 left-0 w-full text-center text-s text-gray-500 italic">
       *No ducks were harmed in the making of this product.*
      </footer>
    </div> 

  );
}
