with open('d4_input.txt', 'r') as f:
    data = f.readlines()


def extract_number_arr(list):
    win_nr_list = []
    lotto_nr_list = []
    lotto_numb_list = []
    for line in list:
        line = line[0:-1] # remove \n
        new_line = line.split(':')
        lotto_numb = int(new_line[0][5:])
        nr_set = new_line[1].split('|')
        win_nr = nr_set[0].split(' ')
        lotto_nr= nr_set[1].split(' ')

        # Clean up the data sets
        win_nr[:] = [item for item in win_nr if item != '']
        lotto_nr[:] = [item for item in lotto_nr if item != '']

        win_nr_list.append(win_nr)
        lotto_nr_list.append(lotto_nr)
        lotto_numb_list.append(lotto_numb)

    return win_nr_list, lotto_nr_list, lotto_numb_list

def update_sets(control_set, copy_set, lotto_numb, matching_nrs, org_set):
    start_copy_at = lotto_numb
    end_copy_at = lotto_numb+matching_nrs
    for nr in range(start_copy_at, end_copy_at):
        control_set[0].append(org_set[0][nr].copy())
        control_set[1].append(org_set[1][nr].copy())
        control_set[2].append(org_set[2][nr])
        copy_set[0].append(org_set[0][nr].copy())
        copy_set[1].append(org_set[1][nr].copy())
        copy_set[2].append(org_set[2][nr])

    return control_set, copy_set

def Calc_Win(facit_list, test_list, lotto_numb, org_set):
    sum_win_list = []
    lotto_wins = []
    control_set = [facit_list[:], test_list[:], lotto_numb]
    copy_set = [[],[],[]]

    while control_set[0] != []:
        facit_set= control_set[0].pop(0)
        test_set = control_set[1].pop(0)
        lotto_numb = control_set[2].pop(0)

        for facit_nr in facit_set:
            for test_nr in test_set:
                if facit_nr == test_nr:
                    lotto_wins.append(1)
        if lotto_wins != []:
            matching_nrs = sum(lotto_wins)
            control_set, copy_set = update_sets(control_set, copy_set, lotto_numb, matching_nrs, org_set)
            lotto_nr.append(2**(matching_nrs-1))
            lotto_wins = []

    sum_wins = sum(sum_win_list)
    nr_lottos = len(org_set[0])+len(copy_set[0])
    return sum_wins, nr_lottos

win_nr, lotto_nr, lotto_numb = extract_number_arr(data)

org_set  = [win_nr.copy(), lotto_nr.copy(), lotto_numb.copy()]
sum_lotto_wins, nr_lottos = Calc_Win(win_nr, lotto_nr, lotto_numb, org_set)

print('sum of lotto wins: ', sum_lotto_wins ,'\n number of lottos: ', nr_lottos)