import heapq
import math


class Node:
    def __init__(self, row, col, parent=None, cost=0, heuristic=0):
        self.row = row
        self.col = col
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

    def __lt__(self, other):
        return self.total_cost < other.total_cost


def get_neighbors(grid, node):
    neighbors = []
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),   # Horizontal and vertical
        (1, 1), (-1, -1), (1, -1), (-1, 1)  # Diagonal
    ]

    for dr, dc in directions:
        newRow, newCol = node.row + dr, node.col + dc
        if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == 1:
            neighbors.append((newRow, newCol))

    return neighbors


def euclidean_distance(node, goal):
    return math.sqrt((node.row - goal[0])**2 + (node.col - goal[1])**2)


def a_star(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start[0], start[1], cost=0, heuristic=euclidean_distance(
        Node(start[0], start[1]), goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if (current_node.row, current_node.col) == goal:
            path = []
            while current_node:
                path.insert(0, (current_node.row, current_node.col))
                current_node = current_node.parent
            return path

        closed_set.add((current_node.row, current_node.col))

        neighbors = get_neighbors(grid, current_node)
        for neighbor_row, neighbor_col in neighbors:
            if (neighbor_row, neighbor_col) in closed_set:
                continue

            new_cost = current_node.cost + 1
            new_node = Node(neighbor_row, neighbor_col, current_node, new_cost,
                            euclidean_distance(Node(neighbor_row, neighbor_col), goal))

            existing_open = [node for node in open_list if (
                node.row, node.col) == (neighbor_row, neighbor_col)]
            if existing_open:
                existing_open = existing_open[0]
                if new_node.total_cost < existing_open.total_cost:
                    open_list.remove(existing_open)
                    heapq.heappush(open_list, new_node)
            else:
                heapq.heappush(open_list, new_node)

            # heapq.heappush(open_list, new_node)

    return None  # No path found


# Given grid and start/destination points
grid = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
]

start = (8, 0)
goal = (0, 0)

path = a_star(grid, start, goal)
if path:
    for node_row, node_col in path:
        # print(f"Row: {node_row}, Col: {node_col}")
        print(f"({node_row}, {node_col})")
else:
    print("No path found.")
