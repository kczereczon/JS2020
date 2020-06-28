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
    print(string)
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
    print(hand_rank_list)
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

    # histogramy rang kart graczy  okresla ile razy wystapila karta o tej samej randze,
    # potrzebne do ustalenia ukladu kart
    hand_rank_histogram = histogram(hand_rank_list)
    # histogramy kolorow kart graczy, jesli 5 in hand_color_histogram.values() == True
    # to wszystkie karty sa jednego koloru
    hand_color_histogram = histogram(hand_color_list)
    # czy karty sa "po kolei" (konieczne w: poker krolewski, pokerze, strit)
    # TODO: zaimplementuj funkcje is_rank_sequence(hand) ktora zwraca True jesli karty sa po kolei
    #       w przeciwnym razie zwraca false. Pobiera liste kart jako parametr
    is_hand_rank_sequence = is_rank_sequence(hand)

    hand_strength = 0  # zwracana zmienna, ja trzeba ustawic
    # ------ sprawdzamy uklad gracza 1:
    # --- sprawdzamy poker krolewski: 5 kart w tym samym kolorze, po kolei, najwyzsza to as
    if((5 in hand_color_histogram.values()) and ('A' in hand_rank_list) and is_hand_rank_sequence):
        hand_strength = 10
    # --- sprawdzamy poker: 5 kart w tym samym kolorze, po kolei
    elif((5 in hand_color_histogram.values()) and is_hand_rank_sequence):
        hand_strength = 9
    # TODO: za pomoca instrukcji elif oraz else sprawdz ponizsze warunki i ustaw
    #       wartosc zmiennej hand_strength:
    #        - sprawdzamy karete: 4 karty tej samej rangi
    #        - sprawdzamy full house: 3 karty tej samej rangi i 2 karty tej samej rangi
    #        - sprawdzamy kolor
    #        - sprawdzamy strit
    #        - sprawdzamy trojke
    #        - sprawdzamy wysoka karte
    #        - sprawdzamy dwie pary
    #        - sprawdzamy jedna pare

    return(hand_strength)


print(is_rank_sequence(
    [['2', 'c'], ['3', 'c'], ['4', 'c'], ['5', 'c'], ['6', 'c']]))
