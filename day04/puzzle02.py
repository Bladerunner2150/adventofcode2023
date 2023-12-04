class Card:
    def __init__(self, card_nr, winning_numbers, scratched_numbers):
        self.card_nr = card_nr
        self.winning_numbers = winning_numbers
        self.scratched_numbers = scratched_numbers
        self.won_cards = self.count_won_cards()

    def count_won_cards(self):
        won_cards = 0
        for number in self.scratched_numbers:
            if number in self.winning_numbers:
                won_cards += 1
        return won_cards

    def __repr__(self):
        return f"Card number: {self.card_nr} | Winning numbers: {self.winning_numbers} | Scratched numbers: {self.scratched_numbers} | Won cards: {self.won_cards}"

initial_cards = []
total_cards = []

def count_winning_cards(card, total_cards):
    for i in range(card.won_cards):
        card_won = initial_cards[card.card_nr + i]
        total_cards.append(card_won)
        count_winning_cards(card_won, total_cards)


def scratch_cards(input):
    inputs = input.split(":")
    card_number = int(inputs[0].split(" ")[-1].strip())
    numbers = inputs[1].split("|")
    winning_numbers = [int(number.strip()) for number in numbers[0].strip().split(" ") if number] # List comprehension, if number = only non-empty strings
    scratched_numbers = [int(number.strip()) for number in numbers[1].strip().split(" ") if number] # List comprehension, if number = only non-empty strings

    return Card(card_number, winning_numbers, scratched_numbers)

with open("input.txt", "r") as file:
    for line in file:
        initial_cards.append(scratch_cards(line.strip()))

total_cards.extend(initial_cards)

for card in initial_cards:
    count_winning_cards(card, total_cards)

print(len(total_cards))