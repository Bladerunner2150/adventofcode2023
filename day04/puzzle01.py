def count_card_points(input):
    points = 0
    inputs = input.split(":")
    numbers = inputs[1].split("|")
    winning_numbers = [int(number.strip()) for number in numbers[0].strip().split(" ") if number] # List comprehension, if number = only non-empty strings
    scratched_numbers = [int(number.strip()) for number in numbers[1].strip().split(" ") if number] # List comprehension, if number = only non-empty strings

    for number in scratched_numbers:
        if number in winning_numbers:
            if points == 0:
                points += 1
            else:
                points *= 2

    return points

with open("input.txt", "r") as file:
    print(sum(count_card_points(line.strip()) for line in file))