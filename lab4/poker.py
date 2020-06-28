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


class Card:
    # słownik symboli unicode
    unicode_dict = {'s': '\u2660', 'h': '\u2665', 'd': '\u2666', 'c': '\u2663'}

    rank = None
    suit = None

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_value(self):
        return [self.rank, self.suit]

    def __str__(self):
        return str(self.rank)+self.unicode_dict[self.suit]


class Deck():

    deck = []

    def __init__(self, *args):
        for figure in figures:
            for color in colors:
                self.deck.append(Card(figure, color))

    def __str__(self):
        string = ""
        for card in self.deck:
            string += str(card) + " "
        return string

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal(self, players):
        for i in range(0, 10):
            players[i % 2].take_card(self.deck.pop())


class Player():

    def __init__(self, money, name=""):
        self.__stack_ = money
        self.__name_ = name
        self.__hand_ = []

    def take_card(self, card):
        self.__hand_.append(card)

    def get_stack_amount(self):
        return self.__stack_

    def get_player_hand_immutable(self):
        return tuple(self.__hand_)

    def cards_to_str(self):
        string = ""
        for card in self.__hand_:
            string += str(card) + " "
        return string


def histogram(text):
    charList = {}
    for char in text:
        if charList.get(char) == None:
            charList[char] = 1
        else:
            charList[char] += 1
    return charList


# slownik wartosci kart w postaci int, dwojka - 2, ...., as - 14
card_rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9, "10": 10, "J": 11, "D": 12,
                    "K": 13, "A": 14}


def figuresSort(elem):
    return figures.index(elem)


def is_rank_sequence(hand):
    hand_rank_list = [card.get_value()[0] for card in hand]
    hand_rank_list.sort(key=figuresSort)

    firstCardRange = hand_rank_list[0]
    indexOfFirstCard = figures.index(firstCardRange)
    if indexOfFirstCard != None:
        for card in hand[1:]:
            indexOfFirstCard += 1
            if figures[indexOfFirstCard] != card.get_value()[0]:
                return False
        return True
    else:
        return False


def get_player_hand_rank(hand):
    hand_rank_list = [card.get_value()[0] for card in hand]
    hand_color_list = [card.get_value()[1] for card in hand]

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
    elif histogram(list(hand_rank_histogram.values())).get(2) == 2:
        hand_strength = 3
    elif 2 in hand_rank_histogram.values():
        hand_strength = 2
    else:
        hand_strength = 1

    return hand_strength
