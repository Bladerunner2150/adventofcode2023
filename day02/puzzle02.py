def find_minimum_cubes(input):
    min_red_count = 0
    min_green_count = 0
    min_blue_count = 0

    inputs = input.split(": ")
    sets = inputs[1].split("; ")

    for set in sets:
        color_sets = set.split(", ")
        for color_set in color_sets:
            color_set = color_set.split(" ")
            color_count = int(color_set[0])
            color = color_set[1]

            if color == "red" and color_count > min_red_count:
                min_red_count = color_count
            elif color == "green" and color_count > min_green_count:
                min_green_count = color_count
            elif color == "blue" and color_count > min_blue_count:
                min_blue_count = color_count

    return min_red_count * min_green_count * min_blue_count

with open("input.txt", "r") as file:
    print(sum(find_minimum_cubes(line.strip()) for line in file))