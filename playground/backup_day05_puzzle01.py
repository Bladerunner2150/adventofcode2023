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

class Seed:
    def __init__(self, seed_id):
        self.seed_id = seed_id
        self.soil = None
        self.fertilizer = None
        self.water = None
        self.light = None
        self.temperature = None
        self.humidity = None
        self.location = None

    def __repr__(self):
        description = f"---\nSeed id:\t\t{self.seed_id}\nSoil:\t\t\t{self.soil}\nFertilizer:\t\t{self.fertilizer}\nWater:\t\t\t{self.water}\nLight:\t\t\t{self.light}\nTemperature:\t\t{self.temperature}\nHumidity:\t\t{self.humidity}\nLocation:\t\t{self.location}\n---\n"
        return description

folder_path = './inputs/sample'
files_lines = {}    
seeds = []

def populate_seed_list(seed_ids):
    for seed_id in seed_ids.split(" "):
        seed = Seed(int(seed_id))
        seeds.append(seed)
    
def calculate_maps():
    # TODO: iterate over all files in the files_lines dict and calculate the maps, below is example for file 1 (seed to soil map), only 2nd line of the map
    map_values = files_lines[filenames[1]]
    for map_value in map_values:
        values = map_value.split(" ")
        source_range = [int(values[1]), int(values[1]) + int(values[2]) - 1]
        target_range = [int(values[0]), int(values[0]) + int(values[2]) - 1]
        for seed in seeds:
            if seed.seed_id >= source_range[0] and seed.seed_id <= source_range[1]:
                seed.soil = seed.seed_id - source_range[0] + target_range[0]
            else:
                seed.soil = seed.seed_id
    # TODO: check seed id first, then soil, then fertilizer, etc.
    print(seeds)

for filename in os.listdir(folder_path):
    with open(os.path.join(folder_path, filename), 'r') as file:
        files_lines[filename] = [line.strip() for line in file]

populate_seed_list(files_lines[filenames[0]][0])

calculate_maps()