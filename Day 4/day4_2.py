import numpy as np
with open('d4_input.txt', 'r') as f:
    data = f.readlines()

def Calc_Win2(facit_list, test_list):
    lotto_wins = []

    for facit_nr in facit_list:
        for test_nr in test_list:
            if facit_nr == test_nr:
                lotto_wins.append(1)
    sum_wins = sum(lotto_wins)
    return sum_wins

sum_cards = np.ones(len(data))
for pos, line in enumerate(data):

    win_nrs, card_nrs = line.split(':')[1].strip().split('|')
    win_nrs = win_nrs.strip().split(' ')
    card_nrs = card_nrs.strip().split(' ')
    # Clean up the data sets
    card_nrs[:] = [item for item in card_nrs if item != '']
    win_nrs[:] = [item for item in win_nrs if item != '']

    wins = Calc_Win2(win_nrs, card_nrs)
    print(wins)
    sum_cards[pos+1:pos+1+wins]+=sum_cards[pos]




print('number of lottos: ', int(sum(sum_cards)))