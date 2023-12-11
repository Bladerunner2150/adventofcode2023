value_arrays = []

def fill_values(input):
    value_arrays.append([int(value) for value in input.split(" ")])

def predict_next_value(values):
    differences = [values.copy()]

    while any(value != 0 for value in differences[-1]):
        differences.append([-(differences[-1][i] - differences[-1][i + 1]) for i in range(len(differences[-1]) - 1)])

    current_prediction = 0

    for value_array in reversed(differences):
        current_prediction += value_array[-1]

    return current_prediction

with open("input.txt", "r") as file:
    for line in file:
        fill_values(line)

print(sum(predict_next_value(values) for values in value_arrays))