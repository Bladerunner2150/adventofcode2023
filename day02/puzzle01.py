max_red = 12
max_green = 13
max_blue = 14

def find_possible_games(input):
    max_red_count = 0
    max_green_count = 0
    max_blue_count = 0

    result = 0
    inputs = input.split(": ")
    game = inputs[0]
    sets = inputs[1].split("; ")

    for set in sets:
        color_sets = set.split(", ")
        for color_set in color_sets:
            color_set = color_set.split(" ")
            color_count = int(color_set[0])
            color = color_set[1]
            if color == "red" and color_count > max_red_count:
                max_red_count = color_count
            elif color == "green" and color_count > max_green_count:
                max_green_count = color_count
            elif color == "blue" and color_count > max_blue_count:
                max_blue_count = color_count

    if max_red_count <= max_red and max_green_count <= max_green and max_blue_count <= max_blue:
        result = int(game.split(" ")[1])

    return result

with open("input.txt", "r") as file:
    print(sum(find_possible_games(line.strip()) for line in file))