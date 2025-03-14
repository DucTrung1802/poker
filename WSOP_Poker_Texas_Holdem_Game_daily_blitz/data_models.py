from dataclasses import dataclass

from enums import Rank, Suit


@dataclass
class Card:
    rank: Rank
    suit: Suit

    def __repr__(cls):
        return f"Card({cls.rank.value}, {cls.suit.value})"
