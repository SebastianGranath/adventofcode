import sys;import re;import numpy as np

def hand_combo(hand):
    combo = []
    for el in hand:
        #print(hand.count(el))
        combo.append(hand.count(el))
        combo = sorted(combo)
    #print(hand, type(combo), combo_strength(combo))
    return combo_strength(combo)

def combo_strength(combo):
    if combo == [1,1,1,2,2]:
        return 'pair', 1
    elif combo == [1,2,2,2,2]:
        return 'two-pair', 2
    elif combo == [1,1,3,3,3]:
        return 'three-of-a-kind', 3
    elif combo == [2,2,3,3,3]:
        return 'full-house', 4
    elif combo == [1,4,4,4,4]:
        return 'four-of-a-kind', 5
    elif combo == [5,5,5,5,5]:
        return 'full-house', 6
    else:
        return 'none', 0

def hand_value(hand):
    card_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
                  'A': 14}
    return [card_order[card] for card in hand]

def compare_combos(combos):
    for combo in combos:
        combo.append(sorted(hand_value(combo[-1])))

    combos = sorted(combos, key=lambda x: (x[0], x[4]))
    return combos

def calculate_bids(combos, bids):
    result = 0

    i = 0
    for combo in combos:
        i += 1
        bid = int(bids[combo[2]])
        result += i * bid

    return result


with open('7.test', 'r') as f:

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

print(combos)
result = calculate_bids(combos, bids)

print(result)
