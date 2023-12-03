# import re

# values = []

# def findCalibrationValues(input):
#     digits = re.findall(r'\d', input)
#     firstAndLast = [digits[0], digits[-1]]
#     return int("".join(firstAndLast))

# with open("input.txt", "r") as file:
#     for line in file:
#         value = findCalibrationValues(line.strip())
#         values.append(value)

# print(sum(values))

import re

def find_calibration_values(input):
    digits = re.findall(r'\d', input)
    first_and_last = [digits[0], digits[-1]]
    return int("".join(first_and_last))

with open("input.txt", "r") as file:
    print(sum(find_calibration_values(line.strip()) for line in file))