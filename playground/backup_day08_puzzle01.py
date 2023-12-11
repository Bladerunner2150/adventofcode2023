from enum import Enum

movement_pattern = []
nodes = []
amount_of_steps = 0

class Direction(Enum):
    Left = 1
    Right = 2

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node name: '{self.name}' | Left: '{self.left}' | Right: '{self.right}'"
    
def fill_nodes(input):
    with open(input, "r") as file:
        for line in file:
            if "=" in line:
                line_parts = line.translate(str.maketrans('', '', '() \n')).split("=")
                name = line_parts[0]
                directions = line_parts[1].split(",")
                nodes.append(Node(name, directions[0], directions[1]))
            elif line != "\n":
                for char in line:
                    if char == "L":
                        movement_pattern.append(Direction.Left)
                    elif char == "R":
                        movement_pattern.append(Direction.Right)

def make_movement():
    global amount_of_steps
    current_node = nodes[0]
    node_index = 0
    print(f"Starting at '{current_node.name}'")
    while current_node.name != "ZZZ":
        direction_to_move = movement_pattern[node_index % len(movement_pattern)]
        if direction_to_move == Direction.Left:
            filtered_nodes = [node for node in nodes if node.name == current_node.left]
            current_node = filtered_nodes[0]
        elif direction_to_move == Direction.Right:
            filtered_nodes = [node for node in nodes if node.name == current_node.right]
            current_node = filtered_nodes[0]
        amount_of_steps += 1
        node_index += 1
        print(f"Step {amount_of_steps}: moved to '{current_node.name}'")
    print(f"Reached ZZZ in {amount_of_steps} steps")

# Optimized version with dictionary
def make_movement_in_dict():
    global amount_of_steps
    node_dict = {node.name: node for node in nodes}
    current_node = node_dict[nodes[0].name]
    node_index = 0
    print(f"Starting at '{current_node.name}'")
    while current_node.name != "ZZZ":
        direction_to_move = movement_pattern[node_index % len(movement_pattern)]
        if direction_to_move == Direction.Left:
            current_node = node_dict[current_node.left]
        elif direction_to_move == Direction.Right:
            current_node = node_dict[current_node.right]
        amount_of_steps += 1
        node_index += 1
        print(f"Step {amount_of_steps}: moved to '{current_node.name}'")
    print(f"Reached ZZZ in {amount_of_steps} steps")

fill_nodes("input.txt")
# make_movement()
make_movement_in_dict()