time = 0
distance = 0

def calculate_ways_to_win_for_race():
    distance_to_reach = distance + 1
    wins = 0
    possible_speed = 1
    for holding_millisecond in range(1, time): # Ignore 0 milliseconds and the last millisecond
        possible_distance = possible_speed * (time - holding_millisecond)
        if possible_distance >= distance_to_reach:
            wins += 1
        possible_speed += 1
    return wins

with open("input.txt", "r") as file:
    for line in file:
        if line.strip().startswith("Time:"):
            time = int(line.split(":")[1].replace(" ", ""))
        elif line.strip().startswith("Distance:"):
            distance = int(line.split(":")[1].replace(" ", ""))

print(calculate_ways_to_win_for_race())
