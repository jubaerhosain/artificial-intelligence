from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

import bfs
import dfs

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


class TwoDArray(BaseModel):
    board: List[List[int]]


@app.post("/bfs")
async def solve(input: TwoDArray):
    print(input)
    solution = bfs.solve_8_puzzle(input.board)
    return solution

@app.post("/dfs")
async def solve(input: TwoDArray):
    print(input)
    solution = dfs.solve_8_puzzle(input.board)
    return solution