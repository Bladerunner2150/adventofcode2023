import os

filenames = [
        '00-seeds.txt',
        '01-seed-to-soil-map.txt',
        '02-soil-to-fertilizer-map.txt',
        '03-fertilizer-to-water-map.txt',
        '04-water-to-light-map.txt',
        '05-light-to-temperature-map.txt',
        '06-temperature-to-humidity-map.txt',
        '07-humidity-to-location-map.txt'
    ]

folder_path = './inputs/actual'
files_lines = {}    
seeds = []

def populate_seed_list(seed_ids):
    range_sets = [list(map(int, seed_ids.split()))[i:i+2] for i in range(0, len(seed_ids.split()), 2)]
    for range_set in range_sets:
        seeds.extend([i for i in range(range_set[0], range_set[0] + range_set[1])])
    
def calculate_maps(filename):
    print(f"Calculating map for {filename}")
    map_values = files_lines[filename]
    for seed_index in range(len(seeds)):
        for map_value in map_values:
            values = map_value.split(" ")
            source_range = [int(values[1]), int(values[1]) + int(values[2]) - 1]
            target_range = [int(values[0]), int(values[0]) + int(values[2]) - 1]
            if seeds[seed_index] >= source_range[0] and seeds[seed_index] <= source_range[1]:
                seeds[seed_index] = seeds[seed_index] - source_range[0] + target_range[0]
                break
    print(f"Final seeds are: {seeds}")

for filename in os.listdir(folder_path):
    with open(os.path.join(folder_path, filename), 'r') as file:
        files_lines[filename] = [line.strip() for line in file]

populate_seed_list(files_lines[filenames[0]][0])
print(f"Initial seeds are: {seeds}")

for filename in filenames[1:]:
    calculate_maps(filename)

print(min(seeds))