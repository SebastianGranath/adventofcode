#  destination range start, the source range start, and the range length
with open('d5input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')
data[:] = [item for item in data if item != '']
seeds = data[0].split(':')[1].split(' ')
# 79 14 55 13 ok
# 81 14 57 13 ok
# 81 53 57 52 ok
# 81 49 53 41 NOK 2nd element
# 74 42 46 34
# 78 42 82 34
# 78 43 82 35
# 82 43 86 35
seeds[:] = [item for item in seeds if item != '']
seeds = [int(x) for x in seeds]
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
        print(line, seeds)
answ = seeds_static[seeds.index(min(seeds))]

# Step 1: Get each map into a separate field





print('seed: ', answ, 'with distance: ', seeds[seeds.index(min(seeds))])