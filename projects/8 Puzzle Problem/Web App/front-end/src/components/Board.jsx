/* eslint-disable react/prop-types */

export default function Board({ board }) {
    return (
        <div className="w-96 h-96 border border-gray-500 m-auto flex items-center justify-center">
            <div className="w-72 h-72 grid grid-cols-3 gap-2">
                {board.map((row, rowIndex) =>
                    row.map((cellValue, colIndex) => (
                        <div
                            key={`${rowIndex}-${colIndex}`}
                            className={`h-20 w-20 flex items-center justify-center border border-gray-500 text-4xl ${
                                cellValue === 0
                                    ? "bg-gray-500 text-white"
                                    : "bg-white text-gray-900"
                            }`}
                        >
                            {cellValue === 0 ? "" : cellValue}
                        </div>
                    ))
                )}
            </div>
        </div>
    );
}
