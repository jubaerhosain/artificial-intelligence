import "./App.css";

import BoardContainer from "./components/BoardContainer";

function App() {
    return (
        <div className="m-auto p-4 max-w-6xl border border-green-100 min-w-max min-h-screen flex flex-col text-center">
            <h1 className="font-extrabold text-6xl text-purple-700">8 Puzzle Game</h1>
            <BoardContainer />
        </div>
    );
}

export default App;
