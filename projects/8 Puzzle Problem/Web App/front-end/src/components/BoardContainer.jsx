import { useEffect, useState } from "react";
import createRandomDistinctArray from "../utils/createRandomGrid";
import axios from "axios";

import Board from "./Board";

const BoardContainer = () => {
    const [board, setBoard] = useState(createRandomDistinctArray());
    const [moves, setMoves] = useState([]);
    const [solveClicked, setSolveClicked] = useState(false);
    const [hasSolution, setHasSolution] = useState(true);

    const reset = () => {
        setHasSolution(true);

        setMoves([]);

        setBoard(createRandomDistinctArray());
    };

    const solvePuzzle = async () => {
        setHasSolution(true);
        setSolveClicked(true);

        if (solveClicked) return;

        console.log("clicked");

        try {
            const response = await axios.post("http://127.0.0.1:8000/brute_force", { board });
            console.log(response.data);

            if (response.data) setMoves(response.data);
            else {
                setHasSolution(false);
                setSolveClicked(false);
            }
        } catch (err) {
            console.log(err);
        }
    };

    useEffect(() => {
        const getEmptyCell = () => {
            let x = 0,
                y = 0;
            for (let i = 0; i <= 2; i++) {
                for (let j = 0; j <= 2; j++) {
                    if (board[i][j] === 0) {
                        (x = i), (y = j);
                        return { x, y };
                    }
                }
            }
        };

        function swap(arr, p1, p2) {
            const temp = arr[p1.x][p1.y];
            arr[p1.x][p1.y] = arr[p2.x][p2.y];
            arr[p2.x][p2.y] = temp;
        }

        const isValidMove = (point) => {
            return point.x >= 0 && point.x <= 2 && point.y >= 0 && point.y <= 2;
        };

        const point = getEmptyCell();

        let currentIndex = 0;
        const interval = setInterval(() => {
            if (currentIndex < moves.length) {
                const move = moves[currentIndex++];

                const tmpBoard = [...[...board]];

                if (move == "left" && isValidMove({ x: point.x, y: point.y - 1 })) {
                    swap(tmpBoard, point, { x: point.x, y: point.y - 1 });
                    point.y -= 1;
                } else if (move == "right" && isValidMove({ x: point.x, y: point.y + 1 })) {
                    swap(tmpBoard, point, { x: point.x, y: point.y + 1 });
                    point.y += 1;
                } else if (move == "up" && isValidMove({ x: point.x - 1, y: point.y })) {
                    swap(tmpBoard, point, { x: point.x - 1, y: point.y });
                    point.x -= 1;
                } else if (move == "down" && isValidMove({ x: point.x + 1, y: point.y })) {
                    swap(tmpBoard, point, { x: point.x + 1, y: point.y });
                    point.x += 1;
                } else {
                    console.log("invalid move");
                }

                setBoard(tmpBoard);
            } else {
                clearInterval(interval);
            }
        }, 1000);

        return () => {
            clearInterval(interval);
            console.log("interval cleared");
        };
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [moves]);

    return (
        <div className="my-10 border border-purple-600 flex flex-row justify-around flex-grow">
            <Board board={board} />

            <div className="w-80 h-60 p-2 space-y-4 flex flex-col items-center justify-around  m-auto">
                {moves.length > 0 && (
                    <div>
                        <div>Solving the puzzle...</div>
                        <div>Move left: 0</div>
                        <div>Estimated time: 3.452232 ms</div>
                    </div>
                )}

                {!hasSolution && <div>No Solution Found</div>}

                <select className="p-2 border border-gray-300 shadow-sm w-60">
                    <option defaultValue={"brute_force"}>Choose an algorithm</option>
                    <option value="US">Brute Force</option>
                    <option value="CA">DFS</option>
                    <option value="FR">BFS</option>
                    <option value="DE">A*</option>
                </select>

                <button
                    onClick={solvePuzzle}
                    disabled={solveClicked}
                    className="p-2 border border-gray-300 shadow-sm w-60"
                >
                    Solve
                </button>
                <button onClick={reset} className="p-2 border border-gray-300 shadow-sm w-60">
                    Reset
                </button>
            </div>
        </div>
    );
};

export default BoardContainer;
