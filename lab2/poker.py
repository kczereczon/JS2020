import random


def deck():
    deck = []
    figures = [
        '2', '3', '4', '5', '6', '7', '8',
        '9', '10', 'J', 'D', 'K', 'A'
    ]

    #c - clubs, d - diamonds, h - hearts, s -spades
    colors = [
        'c',
        'd',
        'h',
        's'
    ]

    for figure in figures:
        for color in colors:
            deck.append({figure, color})

    return deck


def shuffle_deck(deck):
    return random.shuffle(deck)


deck = deck()
print(deck)
shuffle_deck(deck)
print(deck)
