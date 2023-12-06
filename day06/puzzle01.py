from functools import reduce
import operator

times = []
distances = []
ways_to_win = [] # For each race, calculate the number of ways to win

def fill_arrays(line):
    if line.startswith("Time:"):
        times.extend([int(time.strip()) for time in line.split(":")[1].split()])
    elif line.startswith("Distance:"):
        distances.extend([int(distance.strip()) for distance in line.split(":")[1].split()])

def calculate_ways_to_win_for_race(index):
    time = times[index]
    distance_to_reach = distances[index] + 1
    print(f"Calculating race {i + 1} with distance to reach: {distance_to_reach}")
    can_finish = [] # Array of booleans per millisecond
    possible_speed = 1
    for holding_milli_second in range(1, time): # Ignore 0 milliseconds and the last millisecond
        possible_distance = possible_speed * (time - holding_milli_second)
        if possible_distance >= distance_to_reach:
            can_finish.append(True)
        else:
            can_finish.append(False)
        possible_speed += 1
    ways_to_win.append(sum(can_finish))

with open("input.txt", "r") as file:
    for line in file:
        fill_arrays(line.strip())

for i in range(len(times)):
    calculate_ways_to_win_for_race(i)

print(reduce(operator.mul, ways_to_win))
