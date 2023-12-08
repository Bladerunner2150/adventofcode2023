from enum import Enum
import re

graph = {}
graph_movement_pattern = ""

def fill_nodes(input):
    with open(input, "r") as file:
        global graph_movement_pattern
        for line in file:
            if "=" in line:
                line_parts = line.translate(str.maketrans('', '', '() \n')).split("=")
                name = line_parts[0]
                directions = line_parts[1].split(",")
                graph[name] = {'Left': directions[0], 'Right': directions[1]}
            elif line != "\n":
                graph_movement_pattern = re.findall(r'[LR]', line)

def make_movement_using_graph(graph, graph_movement_pattern):
    current_node = list(graph.keys())[0]  # Starting at the first node in the graph
    steps = 0
    print(f"Starting at '{current_node}' with graph {graph}")
    while current_node != 'ZZZ':
        direction_to_move = graph_movement_pattern[steps % len(graph_movement_pattern)]
        if direction_to_move == 'L':
            current_node = graph[current_node]['Left']
        elif direction_to_move == 'R':
            current_node = graph[current_node]['Right']
        steps += 1
        # print(f"Moved {direction_to_move} to '{current_node}' in {steps} steps")
    # for direction in graph_movement_pattern:
    #     if direction == 'L':
    #         current_node = graph[current_node]['Left']
    #     elif direction == 'R':
    #         current_node = graph[current_node]['Right']
    #     steps += 1
    #     if current_node == 'ZZZ':
    #         break
    return steps


fill_nodes("input.txt")
steps_taken = make_movement_using_graph(graph, graph_movement_pattern)
print(steps_taken)