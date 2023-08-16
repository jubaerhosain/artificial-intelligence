import time

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


def bfs(initial_state, target_states):
    solvable_input = is_solvable(initial_state)
    solvable_targets = [is_solvable(target) for target in target_states]

    if solvable_input not in solvable_targets:
        return None

    queue = [(initial_state, [])]
    visited_states = set()

    while queue:
        current_state, path = queue.pop(0)

        if current_state in target_states:
            return path

        visited_states.add(tuple(map(tuple, current_state)))

        for direction in ['up', 'down', 'left', 'right']:
            new_state = move(current_state, direction)
            if tuple(map(tuple, new_state)) not in visited_states:
                queue.append((new_state, path + [direction]))

    return None


def solve_8_puzzle(initial_state):
    start = time.perf_counter()

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

    solution = bfs(initial_state, [target_state1, target_state2])

    if solution:
        print("Solution found!\nMoves:", solution)
    else:
        print("No solution found.")

    end = time.perf_counter()
    print("Execution time is: ", (end-start)*10*3, "ms")

    return solution


if __name__ == '__main__':
    solve_8_puzzle([[1, 2, 3],
          [0, 5, 6],
          [4, 7, 8]])
