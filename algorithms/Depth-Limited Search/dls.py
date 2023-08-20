class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def depth_limited_search(node, goal_value, depth_limit):
    if node.value == goal_value:
        return node.value
    if depth_limit == 0:
        return None
    for child in node.children:
        result = depth_limited_search(child, goal_value, depth_limit - 1)
        if result is not None:
            return result
    return None


# Example usage
# Create a sample tree
root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), Node(5)]
root.children[1].children = [Node(6)]

goal_value = 6
depth_limit = 3  # Set your desired depth limit
result = depth_limited_search(root, goal_value, depth_limit)

if result is not None:
    print(f"Goal value {goal_value} found!")
else:
    print(f"Goal value {goal_value} not found within depth limit.")
