def find_calibration_values(input):
    found_values = []

    num_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }

    for i in range(len(input)):
        if input[i].isdigit():
            found_values.append(input[i])
        else:
            for key, value in num_dict.items():
                if input[i:].startswith(key):
                    found_values.append(value)

    first_and_last = [found_values[0], found_values[-1]]
    return int("".join(first_and_last))

with open("input.txt", "r") as file:
    print(sum(find_calibration_values(line.strip()) for line in file))