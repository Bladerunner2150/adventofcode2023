import os

folder_path = './inputs/sample'
filenames = []
files_lines = {}

def calculate_maps(filename, seed):
    map_values = files_lines[filename]
    for map_value in map_values:
        values = map_value.split()
        source_range = [int(values[1]), int(values[1]) + int(values[2]) - 1]
        target_range = [int(values[0]), int(values[0]) + int(values[2]) - 1]
        if seed >= source_range[0] and seed <= source_range[1]:
            return seed - source_range[0] + target_range[0]
    return seed

for filename in os.listdir(folder_path):
    filenames.append(filename)
    with open(os.path.join(folder_path, filename), 'r') as file:
        files_lines[filename] = [line.strip() for line in file]

# TODO: optimize code, this is too resource intensive
seed_ranges = [list(map(int, files_lines[filenames[0]][0].split()))[i:i+2] for i in range(0, len(files_lines[filenames[0]][0].split()), 2)]
min_seed = float('inf')

for seed_range in seed_ranges:
    for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
        for filename in filenames[1:]:
            seed = calculate_maps(filename, seed)
        min_seed = min(min_seed, seed)

print(min_seed)