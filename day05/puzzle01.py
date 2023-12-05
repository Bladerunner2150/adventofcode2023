import os

folder_path = './inputs/actual'
filenames = []
files_lines = {}    
seeds = []

def populate_seed_list(seed_ids):
    for seed_id in seed_ids.split():
        seeds.append(int(seed_id))
    
def calculate_maps(filename):
    print(f"Calculating map for {filename}")
    map_values = files_lines[filename]
    for seed_index in range(len(seeds)):
        for map_value in map_values:
            values = map_value.split()
            source_range = [int(values[1]), int(values[1]) + int(values[2]) - 1]
            target_range = [int(values[0]), int(values[0]) + int(values[2]) - 1]
            if seeds[seed_index] >= source_range[0] and seeds[seed_index] <= source_range[1]:
                seeds[seed_index] = seeds[seed_index] - source_range[0] + target_range[0]
                break
    print(f"Final seeds are: {seeds}")

for filename in os.listdir(folder_path):
    filenames.append(filename)
    with open(os.path.join(folder_path, filename), 'r') as file:
        files_lines[filename] = [line.strip() for line in file]

populate_seed_list(files_lines[filenames[0]][0])
print(f"Initial seeds are: {seeds}")

for filename in filenames[1:]:
    calculate_maps(filename)

print(min(seeds))