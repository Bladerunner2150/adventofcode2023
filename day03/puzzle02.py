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

def is_adjacent_to_symbol(sc, nc):
    adjacent_x = sc.y == nc.y and (sc.x == nc.x - 1 or sc.x == len(str(nc.value)) + nc.x)
    adjacent_y = (sc.y == nc.y - 1 or sc.y == nc.y + 1) and (sc.x >= nc.x - 1 and sc.x <= nc.x + len(str(nc.value)))
    return adjacent_x or adjacent_y

def count_gears(coordinates):
    result = 0
    symbol_coordinates = [coord for coord in coordinates if coord.value == 0]
    number_coordinates = [coord for coord in coordinates if coord.value != 0]

    for symbol_coord in symbol_coordinates:
        adjacent_numbers = []
        if symbol_coord.symbol == "*":
            for number_coord in number_coordinates:
                if is_adjacent_to_symbol(symbol_coord, number_coord):
                    adjacent_numbers.append(number_coord.value)

            if len(adjacent_numbers) == 2:
                result += adjacent_numbers[0] * adjacent_numbers[1]
    
    return result

y_coordinate = 0
coordinates = []

with open("input.txt", "r") as file:
    for line in file:
        y_coordinate += 1
        coordinates.extend(add_coordinates_to_array(y_coordinate, line.strip()))

print(count_gears(coordinates))