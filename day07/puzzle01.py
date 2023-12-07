from enum import Enum
from collections import Counter

class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

class Hand:
    def __init__(self, cards, bid):
        self.cards = list(map(self.map_card, cards))
        self.bid = bid
        self.type = self.get_type()

    def map_card(self, card):
        if card == "A":
            return 14
        elif card == "K":
            return 13
        elif card == "Q":
            return 12
        elif card == "J":
            return 11
        elif card == "T":
            return 10
        else:
            return int(card)

    def get_type(self):
        hand_type = HandType.HIGH_CARD
        counter = Counter(self.cards)
        duplicates = {char: count for char, count in counter.items() if count > 1}

        for char, count in duplicates.items():
            if len(duplicates.items()) == 1:
                if count == 2:
                    hand_type = HandType.ONE_PAIR
                elif count == 3:
                    hand_type = HandType.THREE_OF_A_KIND
                elif count == 4:
                    hand_type = HandType.FOUR_OF_A_KIND
                elif count == 5:
                    hand_type = HandType.FIVE_OF_A_KIND
            elif len(duplicates.items()) == 2:
                if 3 not in duplicates.values() and count == 2:
                    hand_type = HandType.TWO_PAIRS
                elif count == 3:
                    hand_type = HandType.FULL_HOUSE

        return hand_type

    def __repr__(self):
        return f"Hand: {self.cards} | Bid: {self.bid} | Rank: {self.rank} | Type: {self.type}\n"
    
hands = []
sorted_hands = []
solution = 0

def fill_hands(input):
    inputs = input.split(" ")
    cards = list(inputs[0])
    bid = int(inputs[1])
    hands.append(Hand(cards, bid))

def calculate_winnings():
    global solution
    for i in range(len(sorted_hands)):
        solution += sorted_hands[i].bid * (i + 1)
    
with open("input.txt", "r") as file:
    for line in file:
        fill_hands(line.strip())

sorted_hands = sorted(hands, key=lambda hand: (hand.type.value, hand.cards))
calculate_winnings()
print(solution)