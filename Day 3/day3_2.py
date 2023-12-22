# from 617 to 22 is wrong!
import numpy as np
def NumberIdentify(data):
    nr = []
    nr_list = []
    for l in range(len(data)):
        for c in range(len(data[l])):
            if data[l][c].isnumeric():
                nr.append(data[l][c])
            elif not data[l][c].isnumeric() and nr != []:
                # nr_list.append(''.join(nr))
                res = BoxCheck(c,l,''.join(nr), data)
                if res and res != []:
                    nr_list.append(res)
                    res = []

                nr = []
    return nr_list

def ControlElement(data,start_c,end_c,start_l,end_l):
    truth_array = []
    gear_candidate_star_pos = []
    for el in data[start_l:end_l]:
        for ec in el[start_c:end_c]:
            if not ec.isnumeric() and ec !='.' and ec != '\n':
                if ec == '*':
                    # ec is the element in the row el. Function goes through the line and each char in each line.
                    pass
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
    if part_bool:
        if len(pos_star)>0:
            return num, pos_star
        else:
            return num, []
    else:
        return []




    #
    # Edge case left
    # Edge case right
    # Edge case top row
    # Edge case bottom row

def GetData():
    with open("day3input.txt", 'r')as f:
        data = f.readlines()
    return data


def main():
    data = GetData()
    nr_list = NumberIdentify(data)
    print(nr_list)
    print(sum(np.array(nr_list, 'int')))


main()


