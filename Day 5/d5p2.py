#  destination range start, the source range start, and the range length
with open('d5input.txt', 'r') as f:
    data = f.read()
import matplotlib.pyplot as plt
data = data.split('\n')
data[:] = [item for item in data if item != '']

# Part 2 Mod
def TestInterval(seeds, spacing):
    seeds_new = []
    min_val = 9999999999999999999999
    small_series = []
    while seeds != []:
        if seeds == []:

            continue
        start = seeds.pop(0)
        nr_seeds = seeds.pop(0)
        temp = list(range(start, start + nr_seeds, spacing))
        seeds_new += temp[:]
        short_route = ControlSeeds(temp)
        if short_route <= min_val:
            min_val = short_route
            small_series = [start, nr_seeds]

    return min_val, small_series


def ControlSeeds(seeds):
    seeds_static = seeds.copy()
    seeds_temp = seeds.copy()
    for el, line in enumerate(data):
        if line[0].isnumeric():
            # Get three separate numbers
            line = [int(x) for x in line.split(' ')]

            source_start = line[1]
            source_end = source_start + line[2]
            dest_start = line[0]
            diff = dest_start - source_start

            for pos, seed in enumerate(seeds_temp):
                if source_start <= int(seed) < source_end:
                    seeds[pos] += diff
        else:
            seeds_temp = seeds.copy()
    answ = seeds_static[seeds.index(min(seeds))]  # Returns the shortest path
    return answ

def ControlSeedRange(R):
    A = []
    for el, line in enumerate(data):
        if line[0].isnumeric():
            # Get three separate numbers
            dest,src,sz = [int(x) for x in line.split(' ')]

            src_end = src + sz
            diff = dest - src
            NR = []

            while R:
                (st, end) = R.pop()


                before = (st, min(end,src))
                inter = (max(st,src), min(src_end, end))
                after = (max(src_end, st), end)

                if before[1]>before[0]:
                    NR.append(before)
                if inter[1]>inter[0]:
                    A.append((inter[0]+diff, inter[1]+diff))
                if after[1]>after[0]:
                    NR.append(after)

            R = NR
    return A+R

def BinarySearch(numbers, val):
    first = 0
    last = len(numbers)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if numbers[mid] == val:
            index = mid
        else:
            if val<numbers[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

def GetSeeds(data):
    seeds = data[0].split(':')[1].split(' ')
    seeds[:] = [item for item in seeds if item != '']
    seeds = [int(x) for x in seeds]
    return seeds

def SeedSpacing(seeds, spacing):
    start = seeds.pop(0)
    nr_seeds = seeds.pop(0)
    temp = list(range(start, start + nr_seeds, spacing))
    return temp

def BestSet(seed_set):
    best_cand_index = seed_set.index(min(seed_set))
    best_cand = seed_set[best_cand_index:best_cand_index + 2]
    return best_cand

seeds = GetSeeds(data)
spacing = 10**7
min_dist = []

seed_pairs = list(zip(seeds[::2], seeds[1::2]))
for start, sz in seed_pairs:
    R = [(start, start+sz)]
    R = ControlSeedRange(R)
    min_dist.append(min(R)[0])
answ = min(min_dist)




print('best seed: ', best_seed,'with distance: ', seeds[seeds.index(min(seeds))])

