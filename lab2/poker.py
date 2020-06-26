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


def shuffle_deck(deck: list):
    return random.shuffle(deck)


def deal(deck: list, n: int):
    deals = []
    for i in range(0, n):
        cards = []
        for j in range(0, 5):
            cards.append(deck.pop())
        deals.insert(i, cards)

    return deals


deck = deck()
shuffle_deck(deck)

print(deal(deck, 5))
