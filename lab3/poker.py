import sys
import random

figures = [
    '2', '3', '4', '5', '6', '7', '8',
    '9', '10', 'J', 'D', 'K', 'A'
]
colors = [
    'c',
    'd',
    'h',
    's'
]


def deck():
    deck = []

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


def histogram(string):
    charList = {'a': 1}
    for char in string:
        if charList.get(char) == None:
            charList[char] = 1
        else:
            charList[char] += 1
    return charList


def figuresSort(elem):
    return figures.index(elem)


def is_rank_sequence(hand):
    hand_rank_list = [list(card)[0] for card in hand]
    hand_rank_list.sort(key=figuresSort)

    firstCardRange = hand_rank_list[0]
    indexOfFirstCard = figures.index(firstCardRange)
    if indexOfFirstCard != None:
        for card in hand[1:]:
            indexOfFirstCard += 1
            if figures[indexOfFirstCard] != card[0]:
                return False
        return True
    else:
        return False


def hand_rank(hand):
    hand_rank_list = [list(card)[0] for card in hand]
    hand_color_list = [list(card)[1] for card in hand]

    hand_rank_histogram = histogram(hand_rank_list)
    hand_color_histogram = histogram(hand_color_list)
    is_hand_rank_sequence = is_rank_sequence(hand)

    hand_strength = 0

    if((5 in hand_color_histogram.values()) and ('A' in hand_rank_list) and is_hand_rank_sequence):
        hand_strength = 10
    elif((5 in hand_color_histogram.values()) and is_hand_rank_sequence):
        hand_strength = 9
    elif 4 in hand_rank_histogram.values():
        hand_strength = 8
    elif (3 in hand_rank_histogram.values() and 2 in hand_rank_histogram.values()):
        hand_strength = 7
    elif 5 in hand_color_histogram.values():
        hand_strength = 6
    elif is_hand_rank_sequence:
        hand_strength = 5
    elif 3 in hand_rank_histogram.values():
        hand_strength = 4
    elif 2 in hand_rank_histogram.values():
        newHistogram = list(hand_rank_histogram.values())
        newHistogram.remove(newHistogram.index(2))
        if 2 in newHistogram:
            hand_strength = 3
        else:
            pass
    elif 2 in hand_rank_histogram.values():
        hand_strength = 2
    else:
        hand_strength = 1

    return(hand_strength)


print(hand_rank(
    [['2', 'c'], ['7', 'b'], ['5', 'c'], ['4', 'h'], ['6', 'c']]))
