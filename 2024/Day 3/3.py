import sys
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('3.in', 'r') as f:
    D = f.read().strip()
#print(D)

def part1(D):
    res = re.findall(r"mul\([0-9,]{3,7}\)",D)
    #print(res)
    operations = 0
    for item in res:
        item = item[4:-1].split(',')
        item = list(map(int,item))
        operations += item[0]*item[1]
        
        #print(item)
    return print('part 1: ', operations)

def part2(D):
    pattern_dont = r"don\'t\(\)"
    donts = re.finditer(pattern_dont, D)
    pattern_do = r"do\(\)"
    dos = re.finditer(pattern_do, D)
    dont_end = []
    do_start  = []
    for match in donts:
        start, end = match.span()
        dont_end.append(end)
        #print(f'found dont at {start} to {end}')

    for match in dos:
        start, end = match.span()
        do_start.append(start)
        #print(f'found dos at {start} to {end}')
    
    result = 0
    break_flag = 0
    print(f'end of donts {dont_end}')
    print(f'start of dos {do_start}')
    end_idx = 0
    for idx in dont_end:
        if end_idx > idx:
            continue
        while end_idx < idx:
            if do_start == []:
                end_idx = -1
                break_flag = 1
                break
            else:
                end_idx = do_start.pop(0)
        #print('before operation: ', len(D))
        D = D[:idx] + (end_idx - idx) * '*' + D[end_idx:]
        if not break_flag:
            print(f'remove from {idx} to {end_idx}')
            
            #print('D updated')
        #print('after operation: ', len(D))
        #result += part1(D[:idx])
    print(D)

    part1(D)

    # Cut out the irrelevant parts of the input
    # do is activated from start
     

part1(D)
part2(D)

# fails: 19 604 994, 10 888 683 (too low), 87 519 257  (too high)