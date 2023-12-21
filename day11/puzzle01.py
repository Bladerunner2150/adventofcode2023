import math
from collections import deque

grid = []
amount_of_galaxies = 0
row_indexes_to_insert = []
column_indexes_to_insert = []
galaxy_pairs_dict = {} # Key: galaxy pair, value: array with coordinates of the galaxies in the pair (start and end)

def find_empty_spaces():
    for row_index in range(len(grid)):
        if row_doesnt_contain(row_index, '#'):
            print("Row {} doesn't contain #".format(row_index + 1))
            row_indexes_to_insert.append(row_index)
    for column_index in range(len(grid[0])):
        if column_doesnt_contain(column_index, '#'):
            print("Column {} doesn't contain #".format(column_index + 1))
            column_indexes_to_insert.append(column_index)

def row_doesnt_contain(row_index, char):
    return char not in grid[row_index]

def column_doesnt_contain(column, char):
    return all(row[column] != char for row in grid)

def expand_universe():
    for row_index in row_indexes_to_insert:
        grid.insert(row_index, ['.'] * len(grid[0]))
        # Increase row indexes in place by 1 because a new row was inserted
        row_indexes_to_insert[:] = [i + 1 for i in row_indexes_to_insert]
    for column_index in column_indexes_to_insert:
        for row in grid:
            row.insert(column_index, '.')
        # Increase column indexes in place by 1 because a new column was inserted
        column_indexes_to_insert[:] = [i + 1 for i in column_indexes_to_insert]

def replace_hashtags_with_numbers():
    global amount_of_galaxies
    for row_index, row in enumerate(grid):
        for column_index, char in enumerate(row):
            if char == '#':
                amount_of_galaxies += 1
                grid[row_index][column_index] = amount_of_galaxies
                galaxy_pairs_dict[amount_of_galaxies] = (row_index, column_index)

def bfs(grid, start):
    rows, cols = len(grid), len(grid[0])
    distances = [[-1] * cols for _ in range(rows)]
    queue = deque([start])
    distances[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))

    return distances

def calculate_shortest_paths(grid):
    n = len(galaxy_pairs_dict)
    paths = [[0] * n for _ in range(n)]

    for i in range(1, n + 1):
        distances = bfs(grid, galaxy_pairs_dict[i])
        for j in range(1, n + 1):
            if i != j:
                paths[i - 1][j - 1] = distances[galaxy_pairs_dict[j][0]][galaxy_pairs_dict[j][1]]

    return paths

def concise_paths(paths):
    """
    Remove redundant paths from the matrix of shortest paths
    (e.g. if the shortest path from galaxy 1 to galaxy 2 is 5, then the shortest path from galaxy 2 to galaxy 1 is also 5)
    """
    n = len(paths)
    concise_output = [[0 if j >= i else paths[i][j] for j in range(n)] for i in range(n)]
    return concise_output

def print_universe():
    print("\n".join(["".join(str(value) for value in row) for row in grid]))
    print('    ' + '  '.join([str(i) for i in range(1, len(grid[0]) + 1)]))
    for i, row in enumerate(grid):
        print(str(i + 1).rjust(3) + ' ' + '  '.join(str(value) for value in row))

with open('input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

find_empty_spaces()

print('Row indexes to insert: {}'.format(row_indexes_to_insert))
print('Column indexes to insert: {}'.format(column_indexes_to_insert))

print('Before expansion:')
print_universe()

expand_universe()
replace_hashtags_with_numbers()

print('After expansion:')
print_universe()

amount_of_galaxy_pairs = math.comb(amount_of_galaxies, 2)
print('Number of galaxy pairs: {}'.format(amount_of_galaxy_pairs))
print(galaxy_pairs_dict)

shortest_paths = calculate_shortest_paths(grid)
concise_shortest_paths = concise_paths(shortest_paths)
flattened_grid = [value for row in concise_shortest_paths for value in row]
print(sum(flattened_grid))