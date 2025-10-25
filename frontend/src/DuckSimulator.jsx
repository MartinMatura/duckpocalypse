import "./DuckSimulator.css"
import React, { useState } from "react";
import Header from "./Components/Header";
import SimulationArea from "./Components/SimulationArea";
import StatsPanel from "./Components/StatsPanel";
import StrategiesPanel from "./Components/StrategiesPanel";


export default function App() {
  <div className="text-2xl text-red-600 p-4">🦆 Testing Render</div>

  const [simulationStarted, setSimulationStarted] = useState(false);

  const handleStart = () => setSimulationStarted(true);

  return (
    <div className="flex flex-col h-screen bg-[#fefae0]">
      <Header /> 

      <div className="flex flex-1 min-h-0 overflow-hidden h-full">
          {/* Map/Simulation Area on the left */}
          <div className="flex-grow h-full min-h-0 border-r border-gray-300 flex justify-center items-center">
            <SimulationArea />
          </div>

          {/*Right side stats or strategies panel --> one at a time*/}
          <div className="w-64 bg-[#fff9c4] border border-gray-300 p-4 h-full overflow-y-auto">
          {!simulationStarted ? (
            <StrategiesPanel onStart={handleStart} />
          ) : (
              <StatsPanel />
          )}
        </div>
      </div> 

      <footer className="fixed bottom-2 left-0 w-full text-center text-xs text-gray-500 italic">
       *No ducks were harmed in the making of this product.*
      </footer>
    </div> 

  );
}
