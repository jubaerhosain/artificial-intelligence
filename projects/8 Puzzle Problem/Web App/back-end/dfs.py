import sys
import time

# Set the recursion depth limit to a higher value
sys.setrecursionlimit(100000)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

def is_solvable(puzzle):
    flattened_puzzle = [num for row in puzzle for num in row]
    inversion_count = 0
    for i in range(len(flattened_puzzle)):
        for j in range(i + 1, len(flattened_puzzle)):
            if flattened_puzzle[i] and flattened_puzzle[j] and flattened_puzzle[i] > flattened_puzzle[j]:
                inversion_count += 1
    return inversion_count % 2 == 0


def get_empty_position(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col
            
def is_valid_move(row, col):
    return 0 <= row < 3 and 0 <= col < 3


def move(state, dir):
    new_state = [list(row) for row in state]
    empty_row, empty_col = get_empty_position(state)

    next_row, next_col = directions[dir][0] + empty_row, directions[dir][1] + empty_col

    if (is_valid_move(next_row, next_col)):
        new_state[empty_row][empty_col], new_state[next_row][next_col] = \
            new_state[next_row][next_col], new_state[empty_row][empty_col]

    return new_state


def dfs(current_state, target_states, visited_states, path, depth=0):
    if current_state in target_states:
        return path
    
    print(depth)
    if(depth > 50):
        return None

    if (tuple(map(tuple, current_state)) in visited_states):
        return None

    visited_states.add(tuple(map(tuple, current_state)))

    for direction in ['up', 'down', 'left', 'right']:
        new_state = move(current_state, direction)
        if tuple(map(tuple, new_state)) not in visited_states:
            result = dfs(new_state, target_states, visited_states, path + [direction], depth+1)
            if result:
                return result

    return None  # No solution found


def solve_8_puzzle(initial_state):
    target_state1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    target_state2 = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    
    target_states = [target_state1, target_state2]
    
    start = time.perf_counter()
    
    
    solvable_input = is_solvable(initial_state)
    solvable_targets = [is_solvable(target) for target in target_states]

    if solvable_input not in solvable_targets:
        return None

    solution = dfs(initial_state, target_states, set(), [])

    if solution:
        print("Solution found! Path to goal:")
        print(solution)
    else:
        print("No solution found.")
        
    end = time.perf_counter()
    print("Execution time is: ", (end-start)*10*3, "ms")
    
    return solution


if __name__ == "__main__":
    initial_state = [
        [1, 0, 3],
        [4, 5, 6],
        [2, 7, 8]
    ]

    solve_8_puzzle(initial_state)
