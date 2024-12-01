import sys
import re
with open('12.in', 'r') as f:
    D = f.read().strip().split('\n')
print(D)

spring_map, pattern = map(list, zip(*(row.split(' ') for row in D)))
pattern = [list(map(int, p.split(','))) for p in pattern]


for map, pat in zip(spring_map, pattern):
    # where are the ???
    qm_pos = [el == '?' for el in map]

    # where are the #
    hash_pos = [el == '#' for el in map]

    # What is the 'ajdacent' map?
    adj_map = [qm + hash for qm, hash in zip(qm_pos, hash_pos)]

    for index, el in enumerate(adj_map):
        if el == 1:
            start_index = index
            neighbors = 1
            index += 1
            next_el = adj_map[index]
            while next_el == 1 and index + 1 < len(adj_map):
                if index == len(adj_map):
                    break
                neighbors += 1
                index += 1
                next_el = adj_map[index]
            for ix in range(start_index, index):
                adj_map[ix] = neighbors

            print(adj_map)

    # what is the pattern?
    print(f"Pattern ({len(pat)}): {pat}")
    print(f"Map     ({len(map)}): {map}")
    min_form_length = sum(pat) + len(pat) - 1
    print(f'Length minimal form: {min_form_length}')
    extra_chars = len(map) - min_form_length
    print(f"Extra chars: {extra_chars}")


    print(qm_pos,'\n',hash_pos)
    print(f"Positions where broken pool could be placed {adj_map}")
    input()

    # In how many ways could the pattern be fitted, given condition?
    # Pattern can be built using existing '#'. Check adjacent # to the ?s

    # Condition 1: if pattern is 1,2,1, there must be at least one '.' in between of each broken pool

    # Condition 2: find all permutations of the answer
    print(map, pat)

