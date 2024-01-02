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
    # For a range
    seeds_static = R.copy()
    seeds_temp = R.copy()

    uncontrolled_elements = R

    for el, line in enumerate(data):
        if line[0].isnumeric():
            # Get three separate numbers
            dest,src,range = [int(x) for x in line.split(' ')]

            dest_start = dest
            source_start =src
            source_end = src + range

            diff = dest - src
            rem = []
            if source_start in R:
                before_index = R.index(seeds == source_start)
                before = seeds[0:before_index]
                rem = seeds_temp[before_index:]

            if source_end in R:
                end_index = R.index(seeds == source_end)
                end = seeds[end_index:]
                rem = seeds_temp[:end_index]
            if rem != []:
                rem += diff

        else:
            seeds_temp = seeds.copy()

    answ = seeds_static[seeds.index(min(seeds))]  # Returns the shortest path
    return answ

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
for row in seed_pairs:
    R = list(range(row[0], row[0]+row[1]))
    ControlSeedRange(seeds)
answ = ControlSeedRange(seeds)




print('best seed: ', best_seed,'with distance: ', seeds[seeds.index(min(seeds))])

