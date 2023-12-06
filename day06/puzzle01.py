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
    possible_speed = 1
    wins = 0
    for holding_millisecond in range(1, time): # Ignore 0 milliseconds and the last millisecond
        possible_distance = possible_speed * (time - holding_millisecond)
        if possible_distance >= distance_to_reach:
            wins += 1
        possible_speed += 1
    ways_to_win.append(wins)

with open("input.txt", "r") as file:
    for line in file:
        fill_arrays(line.strip())

for i in range(len(times)):
    calculate_ways_to_win_for_race(i)

print(reduce(operator.mul, ways_to_win))
