with open('d4_input.txt', 'r') as f:
    data = f.readlines()

def extract_number_arr(list):
    win_nr_list = []
    lotto_nr_list = []
    for line in list:
        line = line[0:-1] # remove \n
        new_line = line.split(':')
        nr_set = new_line[1].split('|')
        win_nr = nr_set[0].split(' ')
        lotto_nr= nr_set[1].split(' ')

        # Clean up the data sets
        win_nr[:] = [item for item in win_nr if item != '']
        lotto_nr[:] = [item for item in lotto_nr if item != '']

        win_nr_list.append(win_nr)
        lotto_nr_list.append(lotto_nr)

    return win_nr_list, lotto_nr_list

def Calc_Win(facit_list, test_list):
    sum_win_list = []
    lotto_wins = []
    for lotto_nr, facit_set in enumerate(facit_list):
        for facit_nr in facit_set:
            for test_nr in test_list[lotto_nr]:
                if facit_nr == test_nr:
                    lotto_wins.append(1)
        if lotto_wins != []:
            sum_win_list.append(2**(sum(lotto_wins)-1))
            lotto_wins = []

    sum_wins = sum(sum_win_list)
    return sum_wins

win_nr, lotto_nr = extract_number_arr(data)

sum_lotto_wins = Calc_Win(win_nr,lotto_nr)
print('sum of lotto wins: ', sum_lotto_wins)