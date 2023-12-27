# from 617 to 22 is wrong!
import numpy as np
def NumberIdentify(data):
    nr = []
    nr_list = []
    gear_pos_list = []
    for l in range(len(data)):
        for c in range(len(data[l])):
            if data[l][c].isnumeric():
                nr.append(data[l][c])
            elif not data[l][c].isnumeric() and nr != []:
                # nr_list.append(''.join(nr))
                nr = ''.join(nr)
                res, pos_star = BoxCheck(c,l, nr, data)
                # Here we got
                # - the number
                # - the position
                # - length of the number
                if res and res != []:
                    nr_list.append(res)
                    res = []
                if pos_star and pos_star != []:
                    gear_pos_list.append([nr, pos_star])
                    pos_star = []

                nr = []
    return nr_list, gear_pos_list

def ControlElement(data,start_c,end_c,start_l,end_l):
    truth_array = []
    gear_candidate_star_pos = []
    for count_l, el in enumerate(data[start_l:end_l]):
        for count_c, ec in enumerate(el[start_c:end_c]):
            if not ec.isnumeric() and ec !='.' and ec != '\n':
                if ec == '*':
                    # ec is the element in the row el. Function goes through the line and each char in each line.
                    gear_candidate_star_pos.append([start_c+count_c, start_l+count_l])

                    #gear_candidate_star_pos.append([ec, el]) # Appending coordinate of star for gear_candidate
                truth_array.append('1')

    return any(truth_array), gear_candidate_star_pos

def BoxCheck(c, l, num, data):
    c = c -len(num)
   # Left Case
    if c == 0: start_c = c
    else: start_c = c -1
   # Right Case
    if c+len(num) == len(data[l]): end_c = c+len(num)
    else: end_c = c+len(num)+1

   # Top Case
    if l == 0: start_l = l
    else: start_l = l-1
   # Bottom Case
    if l == len(data[l]): end_l = l+1
    else: end_l = l+2

    part_bool, pos_star = ControlElement(data, start_c, end_c, start_l, end_l)

    # Here we have the num, and the pos

    if part_bool:
        if len(pos_star)>0:
            return num, pos_star
        else:
            return num, []
    else:
        return [], []




    #
    # Edge case left
    # Edge case right
    # Edge case top row
    # Edge case bottom row

def GetData():
    with open("day3input.txt", 'r')as f:
        data = f.readlines()
    return data

def GearMulti(list):
    gear = []
    for el_index, el in enumerate(list):
        gear_pos = list[el_index][1][0]
        for el_index2, el2 in enumerate(list):
            if el_index2 == el_index:
                pass
            elif gear_pos == list[el_index2][1][0]:
                gear.append(int(list[el_index][0])*int(list[el_index2][0]))

    res = []
    [res.append(x) for x in gear if x not in res]
    gear_sum = sum(res)
    return gear_sum



def main():
    data = GetData()
    nr_list, gear_pos_list = NumberIdentify(data)
    gear_sum = GearMulti(gear_pos_list)




    print(nr_list)
    print(sum(np.array(nr_list, 'int')))
    print('Gear Ratio: ', gear_sum)


main()


