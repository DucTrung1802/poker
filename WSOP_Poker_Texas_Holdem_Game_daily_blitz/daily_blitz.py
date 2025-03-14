from typing import List
from itertools import combinations
from collections import Counter

from data_models import Card
from enums import Rank, Suit, HandType


def parse_card(input_str: str) -> List[Card]:
    input_str = str.lower(input_str)

    suit_mapping = {"c": Suit.C, "r": Suit.R, "b": Suit.B, "t": Suit.T}
    rank_mapping = {
        "2": Rank._2,
        "3": Rank._3,
        "4": Rank._4,
        "5": Rank._5,
        "6": Rank._6,
        "7": Rank._7,
        "8": Rank._8,
        "9": Rank._9,
        "10": Rank._10,
        "j": Rank._J,
        "q": Rank._Q,
        "k": Rank._K,
        "a": Rank._A,
    }

    result = []
    i = 0
    while i < len(input_str):
        # 0 or 1 will be considered as 10
        if input_str[i] in ("0", "1"):
            rank_str = "10"
        else:
            rank_str = input_str[i]

        i += 1

        # Ensure valid rank
        if rank_str.lower() not in rank_mapping:
            raise ValueError(f"Invalid rank: {rank_str}")

        # Ensure there is a suit character after the rank
        if i >= len(input_str):
            raise ValueError("Suit character missing after rank")

        suit_char = input_str[i].lower()
        i += 1  # Move to next character

        # Ensure valid suit
        if suit_char not in suit_mapping:
            raise ValueError(f"Invalid suit: {suit_char}")

        result.append(Card(rank_mapping[rank_str.lower()], suit_mapping[suit_char]))

    return result


def calculate_poker_point(hand: List[Card]) -> int:
    # print(hand)

    if len(hand) != 5:
        return 0  # Invalid hand

    # Extract ranks and suits
    ranks = sorted([card.rank.value for card in hand])
    suits = [card.suit for card in hand]

    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)

    is_flush = len(suit_counts) == 1  # All cards have the same suit
    is_straight = ranks == list(range(ranks[0], ranks[0] + 5)) or ranks == [
        14,
        2,
        3,
        4,
        5,
    ]
    is_royal = is_flush and ranks == [10, 11, 12, 13, 14]  # A, K, Q, J, 10

    # Determine hand ranking
    if is_royal:
        return (HandType.ROYAL_FLUSH.name, HandType.ROYAL_FLUSH.value)
    if is_flush and is_straight:
        return HandType.STRAIGHT_FLUSH.value
    if 4 in rank_counts.values():
        return HandType.FOUR_OF_A_KIND.value
    if 3 in rank_counts.values() and 2 in rank_counts.values():
        return HandType.FULL_HOUSE.value
    if is_flush:
        return HandType.FLUSH.value
    if is_straight:
        return HandType.STRAIGHT.value
    if 3 in rank_counts.values():
        return HandType.THREE_OF_A_KIND.value
    if list(rank_counts.values()).count(2) == 2:
        return HandType.TWO_PAIR.value
    if 2 in rank_counts.values():
        return HandType.ONE_PAIR.value

    return HandType.HIGH_CARD.value


def calculate_poker_point_for_hands(hand_list: List[List[Card]]) -> int:
    best_hand = max(hand_list, key=lambda hand: calculate_poker_point(hand))
    return calculate_poker_point(best_hand)


# Example usage
def main():
    while True:
        card_string = input("Input card string: ")
        # card_string = "ac2b3r4tjc5b6r9ckc"
        card_list = []

        if card_string == "quit":
            exit(0)
        elif card_string == "sp":
            card_list = parse_card("ac2b3r4tjc5b6r9ckc")
        else:
            card_list = parse_card(card_string)

        if len(card_list) != 9:
            print("Invalid card string. Expected total 9 cards.")
            continue

        left_combination: List[Card] = card_list[:5] + card_list[5:7]
        right_combination: List[Card] = card_list[:5] + card_list[7:9]

        left_point = calculate_poker_point_for_hands(
            list(combinations(left_combination, 5))
        )
        right_point = calculate_poker_point_for_hands(
            list(combinations(right_combination, 5))
        )

        if left_point > right_point:
            print("LEFT")
        else:
            print("RIGHT")


if __name__ == "__main__":
    main()
