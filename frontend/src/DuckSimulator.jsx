import "./DuckSimulator.css"
import React, { useState } from "react";
import Header from "./Components/Header";
import SimulationArea from "./Components/SimulationArea";
import StatsPanel from "./Components/StatsPanel";
import StrategiesPanel from "./Components/StrategiesPanel";


export default function App() {
  const [simulationStarted, setSimulationStarted] = useState(false);

  const handleStart = () => setSimulationStarted(true);

  return (
    <div className="flex flex-col h-screen bg-[#fefae0]">
      <Header /> 

      <div className="flex flex-1">
          {/* Map/Simulation Area on the left */}
          <div className="flex-1 flex items-center justify-center">
            <SimulationArea />
          </div>

          {/*Right side stats or strategies panel*/}
          <div className="w-64 bg-[#fff9c4] border border-gray-200 p-4">
            {simulationStarted ? (
              <StatsPanel />
            ) : (
              <StrategiesPanel onStart={handleStart} />
            )}
          </div>
        </div>
      </div>        
  );
}
