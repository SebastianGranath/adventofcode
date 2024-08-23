import sys;
import re;
import numpy as np


def hand_combo(hand):
    combo = []
    j_count = 0
    for el in hand:
        if el == 'J':
            j_count += 1
        combo.append(hand.count(el))
        combo = sorted(combo)
    # print(hand, type(combo), combo_strength(combo))
    return combo_strength(combo, j_count)


def combo_strength(combo, j_count):
    if combo == [1, 1, 1, 2, 2]:
        if j_count == 1:
            return 'three-of-a-kind', 3
        if j_count == 2:
            return 'three-of-a-kind', 3
        else:
            return 'pair', 1
    elif combo == [1, 2, 2, 2, 2]:
        if j_count == 1:
            return 'full-house', 4
        if j_count == 2:
            return 'four-of-a-kind', 5
        else:
            return 'two-pair', 2
    elif combo == [1, 1, 3, 3, 3]:
        if j_count == 1:
            return 'four-of-a-kind', 5  # Skip over full house
        elif j_count == 3:
            return 'four-of-a-kind', 5
        else:
            return 'three-of-a-kind', 3

    elif combo == [2, 2, 3, 3, 3]:
        if j_count == 3:
            return 'five-of-a-kind', 6  # IF three J:s, get score 6
        elif j_count == 2:
            return 'five-of-a-kind', 6
        else:
            return 'full-house', 4
    elif combo == [1, 4, 4, 4, 4]:
        if j_count == 4:
            return 'five-of-a-kind', 6
        elif j_count == 1:
            return 'five-of-a-kind', 6
        else:
            return 'four-of-a-kind', 5
    elif combo == [5, 5, 5, 5, 5]:
        return 'five-of-a-kind', 6
    else:
        if j_count == 1:
            return 'pair', 1
        else:
            return 'none', 0


def hand_value(hand):
    # card_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,'A': 14}
    card_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13,
                  'A': 14}  # Adjusted for p2
    return [card_order[card] for card in hand]


def compare_combos(combos):
    for combo in combos:
        combo.append(hand_value(combo[-1]))

    # for hand in combos:
    #     hand_str, _, _, _, cards = hand
    #
    #     if hand_str == 2:
    #         # Step 1: Identify the kicker (the card that appears only once)
    #         kicker = [card for card in cards if cards.count(card) == 1][0]
    #
    #         # Step 2: Collect the remaining cards, excluding the kicker
    #         remaining_cards = [card for card in cards if card != kicker]
    #
    #         # Step 3: Sort the remaining cards in descending order
    #         remaining_cards.sort(reverse=True)
    #
    #         # Step 4: Add the kicker to the end of the sorted list
    #         sorted_hand = remaining_cards + [kicker]
    #         hand[4] = sorted_hand

    # calulating two pairs wrong.
    combos = sorted(combos, key=lambda x: (x[0], x[4]))

    return combos


def calculate_bids(combos, bids):
    result = 0

    i = 0
    for combo in combos:
        i += 1
        bid = int(bids[combo[2]])
        result += i * bid
        combo.append([i, bid, i * bid])

    return result, combos


with open('7.in', 'r') as f:
    D = f.read().strip()

D = D.split()
hands = D[0::2]
bids = D[1::2]

combos = []
hand_rank = []

for hand in hands:
    combo, combo_pwr = hand_combo(hand)
    hand_rank.append([combo_pwr, hands.index(hand)])
    combos.append([combo_pwr, combo, hands.index(hand), hand])

combos = compare_combos(combos)

result, combos = calculate_bids(combos, bids)

for combo in combos:
    print(combo)
print(result)
print('fail:', '253943137', '254082230')
