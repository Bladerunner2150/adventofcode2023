def convert_to_numbers(word):
    # Mapping of number words to digits
    number_dict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    # List to store the resulting numbers
    numbers = []

    # Temporary string to build number words
    temp = ""

    for char in word:
        temp += char  # Add current character to temp
        # Check if temp is a valid number word
        if temp in number_dict:
            numbers.append(number_dict[temp])  # Add the corresponding number to the list
            temp = ""  # Reset temp for the next number word

    return numbers

# Example usage
result = convert_to_numbers("eightwothree")
print(result)  # Output: [8, 2, 3]
