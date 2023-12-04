import re

pattern = re.compile(r'\d+|[^.\s]') # Find all numbers or non-period symbols

class Coordinate:
    def __init__(self, x, y, value, symbol):
        self.x = x
        self.y = y
        self.value = value
        self.symbol = symbol

    def __repr__(self):
        return f"X: {self.x} | Y: {self.y} | Value: {self.value} | Symbol: {self.symbol}"

def add_coordinates_to_array(y_coordinate, input):
    coordinates = []
    for match in pattern.finditer(input):
        x_coordinate = match.start() + 1
        actualvalue = match.group()
        intvalue = int(actualvalue) if actualvalue.isdigit() else 0
        coordinates.append(Coordinate(x_coordinate, y_coordinate, intvalue, actualvalue))
    return coordinates

def is_adjacent_x(sc, nc):
    # Check if symbol coordinate is to the left or right of the number coordinate
    return sc.y == nc.y and (sc.x == nc.x - 1 or sc.x == len(str(nc.value)) + nc.x)

def is_adjacent_y(sc, nc):
    # Check if symbol coordinate is above or below the number coordinate and within the number coordinate's length + 1 (for diagonal)
    return (sc.y == nc.y - 1 or sc.y == nc.y + 1) and (sc.x >= nc.x - 1 and sc.x <= nc.x + len(str(nc.value)))

def count_engine_parts(coordinates):
    result = 0
    symbol_coordinates = [coord for coord in coordinates if coord.value == 0]
    number_coordinates = [coord for coord in coordinates if coord.value != 0]
    for number_coord in number_coordinates:
        if any(is_adjacent_x(symbol_coord, number_coord) or is_adjacent_y(symbol_coord, number_coord) for symbol_coord in symbol_coordinates):
            result += number_coord.value
    return result

y_coordinate = 0
coordinates = []

with open("input.txt", "r") as file:
    for line in file:
        y_coordinate += 1
        coordinates.extend(add_coordinates_to_array(y_coordinate, line.strip()))

print(count_engine_parts(coordinates))