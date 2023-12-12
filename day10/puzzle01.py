from enum import Enum, auto
import time

class PipeData:
    def __init__(self, pipe_type, available_directions):
        self.pipe_type = pipe_type
        self.available_directions = available_directions

class Pipe(Enum):
    VERTICAL = '|'
    HORIZONTAL = '-'
    NORTH_EAST_BEND = 'L'
    NORTH_WEST_BEND = 'J'
    SOUTH_EAST_BEND = 'F'
    SOUTH_WEST_BEND = '7'
    GROUND = '.'
    START = 'S'

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

grid = []
grid_dict = {}
starting_coords = None

def populate_grid_dict():
    for y, row in enumerate(grid):
        for x, pipe in enumerate(row):
            pipe_data = PipeData(pipe, [])
            if pipe == Pipe.VERTICAL:
                pipe_data.available_directions = [Direction.UP, Direction.DOWN]
            elif pipe == Pipe.HORIZONTAL:
                pipe_data.available_directions = [Direction.LEFT, Direction.RIGHT]
            elif pipe == Pipe.NORTH_EAST_BEND:
                pipe_data.available_directions = [Direction.UP, Direction.RIGHT]
            elif pipe == Pipe.NORTH_WEST_BEND:
                pipe_data.available_directions = [Direction.UP, Direction.LEFT]
            elif pipe == Pipe.SOUTH_EAST_BEND:
                pipe_data.available_directions = [Direction.DOWN, Direction.RIGHT]
            elif pipe == Pipe.SOUTH_WEST_BEND:
                pipe_data.available_directions = [Direction.DOWN, Direction.LEFT]
            elif pipe == Pipe.START:
                pipe_data.available_directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
            elif pipe == Pipe.GROUND:
                pipe_data.available_directions = []
            grid_dict[(x, y)] = pipe_data

def find_start():
    global starting_coords
    for coords, pipe_data in grid_dict.items():
        if pipe_data.pipe_type == Pipe.START:
            starting_coords = coords
        
def can_go_left(x, y):
    target_pipe_type = grid_dict[(x - 1, y)].pipe_type
    return (
        target_pipe_type == Pipe.START or
        (
            target_pipe_type != Pipe.GROUND and
            (
                target_pipe_type == Pipe.HORIZONTAL or 
                target_pipe_type == Pipe.NORTH_EAST_BEND or
                target_pipe_type == Pipe.SOUTH_EAST_BEND
            )
        )
    )

def can_go_right(x, y):
    target_pipe_type = grid_dict[(x + 1, y)].pipe_type
    return (
        target_pipe_type == Pipe.START or
        (
            target_pipe_type != Pipe.GROUND and
            (
                target_pipe_type == Pipe.HORIZONTAL or
                target_pipe_type == Pipe.NORTH_WEST_BEND or
                target_pipe_type == Pipe.SOUTH_WEST_BEND
            )
        )
    )

def can_go_up(x, y):
    target_pipe_type = grid_dict[(x, y - 1)].pipe_type
    return (
        target_pipe_type == Pipe.START or
        (
            target_pipe_type != Pipe.GROUND and
            (
                target_pipe_type == Pipe.VERTICAL or
                target_pipe_type == Pipe.SOUTH_WEST_BEND or
                target_pipe_type == Pipe.SOUTH_EAST_BEND
            )
        )
    )

def can_go_down(x, y):
    target_pipe_type = grid_dict[(x, y + 1)].pipe_type
    return (
        target_pipe_type == Pipe.START or
        (
            target_pipe_type != Pipe.GROUND and
            (
                target_pipe_type == Pipe.VERTICAL or
                target_pipe_type == Pipe.NORTH_WEST_BEND or
                target_pipe_type == Pipe.NORTH_EAST_BEND
            )
        )
    )

def follow_pipes():
    amount_of_steps = 0
    back_at_start = False
    previous_direction = None
    max_x = max(coords[0] for coords in grid_dict.keys())
    max_y = max(coords[1] for coords in grid_dict.keys())
    x, y = starting_coords
    print("Starting at", x, y)
    while not back_at_start:
        current_pipe = grid_dict[(x, y)]

        if previous_direction is Direction.LEFT and Direction.RIGHT in current_pipe.available_directions:
            current_pipe.available_directions.remove(Direction.RIGHT)
        elif previous_direction is Direction.RIGHT and Direction.LEFT in current_pipe.available_directions:
            current_pipe.available_directions.remove(Direction.LEFT)
        elif previous_direction is Direction.UP and Direction.DOWN in current_pipe.available_directions:
            current_pipe.available_directions.remove(Direction.DOWN)
        elif previous_direction is Direction.DOWN and Direction.UP in current_pipe.available_directions:
            current_pipe.available_directions.remove(Direction.UP)

        print(f"Current pipe: {current_pipe.pipe_type} at {x}, {y} with available directions {current_pipe.available_directions}")

        if current_pipe.pipe_type == Pipe.START and amount_of_steps > 0:
            print("Back at start!")
            back_at_start = True
        elif Direction.LEFT in current_pipe.available_directions and x > 0 and can_go_left(x, y):
            print("Going left")
            previous_direction = Direction.LEFT
            x -= 1
            amount_of_steps += 1
        elif Direction.RIGHT in current_pipe.available_directions and x < max_x and can_go_right(x, y):
            print("Going right")
            previous_direction = Direction.RIGHT
            x += 1
            amount_of_steps += 1
        elif Direction.UP in current_pipe.available_directions and y > 0 and can_go_up(x, y):
            print("Going up")
            previous_direction = Direction.UP
            y -= 1
            amount_of_steps += 1
        elif Direction.DOWN in current_pipe.available_directions and y < max_y and can_go_down(x, y):
            print("Going down")
            previous_direction = Direction.DOWN
            y += 1
            amount_of_steps += 1
    return amount_of_steps

with open("input.txt", "r") as file:
    for line in file:
        grid.append([Pipe(char) for char in line.strip('\n')])

populate_grid_dict()
find_start()
print(follow_pipes() / 2)