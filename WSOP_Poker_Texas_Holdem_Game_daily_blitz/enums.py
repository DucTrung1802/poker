from enum import Enum


class Rank(Enum):
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    _J = 11
    _Q = 12
    _K = 13
    _A = 14


class Suit(Enum):
    C = "heart"  # CƠ
    R = "diamond"  # RÔ
    B = "spade"  # BÍCH
    T = "club"  # TÉP


class HandType(Enum):
    ROYAL_FLUSH = 10  # A, K, Q, J, 10 of the same suit
    STRAIGHT_FLUSH = 9  # Five consecutive cards of the same suit
    FOUR_OF_A_KIND = 8  # Four cards of the same rank
    FULL_HOUSE = 7  # Three of a kind + a pair
    FLUSH = 6  # Five cards of the same suit (not consecutive)
    STRAIGHT = 5  # Five consecutive cards of mixed suits
    THREE_OF_A_KIND = 4  # Three cards of the same rank
    TWO_PAIR = 3  # Two different pairs
    ONE_PAIR = 2  # One pair
    HIGH_CARD = 1  # Highest individual card when no other hand is made
