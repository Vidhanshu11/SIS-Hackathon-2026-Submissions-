import { useState } from 'react';
import { 
  Shield, 
  Menu, 
  Map as MapIcon, 
  Zap, 
  AlertTriangle, 
  Terminal 
} from 'lucide-react';

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [currentTab, setCurrentTab] = useState('airspace');

  const renderContent = () => {
    switch(currentTab) {
      case 'missions':
        return (
          <div className="flex-1 flex items-center justify-center bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-slate-900 via-slate-950 to-slate-950">
            <div className="text-center space-y-4">
              <div className="inline-block p-6 rounded-full bg-sky-500/5 border border-sky-500/20">
                <Terminal className="w-16 h-16 text-sky-500/50" />
              </div>
              <div className="space-y-2">
                <h2 className="text-xl font-bold text-slate-200 tracking-tight">MISSION LOGS</h2>
                <p className="text-slate-500 font-mono text-sm">[ No missions available ]</p>
              </div>
            </div>
          </div>
        );
      case 'incidents':
        return (
          <div className="flex-1 flex items-center justify-center bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-slate-900 via-slate-950 to-slate-950">
            <div className="text-center space-y-4">
              <div className="inline-block p-6 rounded-full bg-sky-500/5 border border-sky-500/20">
                <AlertTriangle className="w-16 h-16 text-sky-500/50" />
              </div>
              <div className="space-y-2">
                <h2 className="text-xl font-bold text-slate-200 tracking-tight">INCIDENTS</h2>
                <p className="text-slate-500 font-mono text-sm">[ No incidents reported ]</p>
              </div>
            </div>
          </div>
        );
      default:
        return (
          <div className="flex-1 flex items-center justify-center bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-slate-900 via-slate-950 to-slate-950">
            <div className="text-center space-y-4 animate-pulse">
              <div className="inline-block p-6 rounded-full bg-sky-500/5 border border-sky-500/20">
                <MapIcon className="w-16 h-16 text-sky-500/50" />
              </div>
              <div className="space-y-2">
                <h2 className="text-xl font-bold text-slate-200 tracking-tight">TACTICAL MAP OFFLINE</h2>
                <p className="text-slate-500 font-mono text-sm">[ WAITING FOR GEOSPATIAL ENGINE... ]</p>
              </div>
            </div>
          </div>
        );
    }
  };

  return (
    <div className="flex h-screen w-screen bg-slate-950 text-slate-200 overflow-hidden font-sans selection:bg-sky-500/30">
      
      {/* SIDEBAR - The "Cockpit" Controls */}
      <aside 
        className={`
          ${isSidebarOpen ? 'w-80' : 'w-0'} 
          bg-slate-900/50 backdrop-blur-md border-r border-slate-800 
          transition-all duration-300 ease-in-out flex flex-col z-20 relative
        `}
      >
        {/* Header Section */}
        <div className="p-5 border-b border-slate-800/60 flex items-center gap-3 bg-slate-900/80">
          <div className="p-2.5 bg-sky-500/10 rounded-lg border border-sky-500/20 shadow-[0_0_15px_rgba(14,165,233,0.15)]">
            <Shield className="w-6 h-6 text-sky-400" />
          </div>
          <div className="overflow-hidden">
            <h1 className="font-bold text-lg text-white tracking-wider font-mono">AIRGUARD</h1>
            <div className="flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
              <p className="text-[10px] text-emerald-500 font-mono tracking-widest uppercase">System Online</p>
            </div>
          </div>
        </div>

        {/* Scrollable Content Area */}
        <div className="flex-1 overflow-y-auto p-4 space-y-6">
          
          {/* Status Card (Placeholder for Real Data) */}
          <div className="bg-slate-800/40 rounded-xl p-4 border border-slate-700/50 hover:border-sky-500/30 transition-colors group">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-mono text-slate-400 uppercase group-hover:text-sky-400 transition-colors">Risk Level</span>
              <span className="flex items-center gap-1 text-emerald-400 text-xs font-bold bg-emerald-500/10 px-2 py-1 rounded border border-emerald-500/20">
                <Shield className="w-3 h-3" /> SAFE
              </span>
            </div>
            
            {/* Fake Graph/Bar */}
            <div className="space-y-1">
               <div className="h-1.5 w-full bg-slate-700/50 rounded-full overflow-hidden">
                 <div className="h-full bg-emerald-500 w-[20%] shadow-[0_0_10px_rgba(16,185,129,0.5)]"></div>
               </div>
               <div className="flex justify-between text-[10px] text-slate-500 font-mono">
                 <span>MIN</span>
                 <span>CRITICAL</span>
               </div>
            </div>
          </div>

          {/* Action Menu (Mock Links) */}
          <nav className="space-y-1">
            <button onClick={() => setCurrentTab('airspace')} className={`w-full px-3 py-2 rounded-lg text-sm font-medium flex items-center gap-3 transition-colors ${currentTab === 'airspace' ? 'bg-sky-500/10 text-sky-400 border border-sky-500/20' : 'text-slate-400 hover:text-white hover:bg-slate-800/50'}`}>
              <MapIcon className="w-4 h-4" />
              <span>Live Airspace</span>
            </button>
            <button onClick={() => setCurrentTab('missions')} className={`w-full px-3 py-2 rounded-lg text-sm font-medium flex items-center gap-3 transition-colors ${currentTab === 'missions' ? 'bg-sky-500/10 text-sky-400 border border-sky-500/20' : 'text-slate-400 hover:text-white hover:bg-slate-800/50'}`}>
              <Terminal className="w-4 h-4" />
              <span>Mission Logs</span>
            </button>
            <button onClick={() => setCurrentTab('incidents')} className={`w-full px-3 py-2 rounded-lg text-sm font-medium flex items-center gap-3 transition-colors ${currentTab === 'incidents' ? 'bg-sky-500/10 text-sky-400 border border-sky-500/20' : 'text-slate-400 hover:text-white hover:bg-slate-800/50'}`}>
              <AlertTriangle className="w-4 h-4" />
              <span>Incidents</span>
            </button>
          </nav>

          {/* AI Chat Placeholder */}
          <div className="mt-auto pt-4 border-t border-slate-800/50">
             <div className="h-40 border border-dashed border-slate-700 rounded-lg flex flex-col items-center justify-center text-slate-600 gap-2 bg-slate-900/30">
                <Zap className="w-6 h-6 opacity-50" />
                <span className="text-xs font-mono">CAPTAIN ARJUN OFFLINE</span>
             </div>
          </div>

        </div>
        
        {/* Footer */}
        <div className="p-3 bg-slate-950 border-t border-slate-800 text-[10px] text-slate-600 font-mono text-center">
          TEAM DAEMONS // SKYHACKERS 2026
        </div>
      </aside>

      {/* MAIN CONTENT - The Map Viewport */}
      <main className="flex-1 relative bg-slate-950 flex flex-col h-full">
        
        {/* Top Navbar Overlay */}
        <div className="absolute top-4 left-4 z-[1000]">
           <button 
             onClick={() => setIsSidebarOpen(!isSidebarOpen)}
             className="p-2.5 bg-slate-900/90 text-slate-200 rounded-lg border border-slate-700 shadow-xl backdrop-blur-md hover:bg-slate-800 hover:text-white transition-all hover:scale-105 active:scale-95"
           >
             <Menu className="w-5 h-5" />
           </button>
        </div>

        {/* MAP PLACEHOLDER (Until we build MapEngine) */}
        {renderContent()}

      </main>
    </div>
  );
}

export default App;