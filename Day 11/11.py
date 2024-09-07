import sys
import re

def get_index(D):
    rows_index_to_insert = []
    column_index_to_insert = []
    for r, row in enumerate(D):
        if row.count(row[0]) == len(row):
            print('All dots on row: ', r)
            rows_index_to_insert.append(r)
    for c, col in enumerate(zip(*D)):
        if col.count(col[0]) == len(col):
            print('All dots on col: ', c)
            column_index_to_insert.append(c)
    return rows_index_to_insert, column_index_to_insert

def insert_space_row(D, rows_index_to_insert):
    i_count = 0
    for i, el in enumerate(rows_index_to_insert):
        D.insert(el+i_count, len(D[rows_index_to_insert[0]])*'*')
        i_count += 1
    return D

def insert_space_col(D, column_index_to_insert):
    i_count = 0
    for i, el in enumerate(column_index_to_insert):
        for r, row in enumerate(D):

            D[r] = D[r][:el+i_count] + '*' + D[r][el+i_count:]
        i_count += 1
    return D


def get_nodes(D):
    nodes = []
    for r, row in enumerate(D):
        for c, el in enumerate(row):
            if el == '#':
                nodes.append([r, c])
    return nodes


def get_pairs(nodes):
    pairs = []
    for c, node in enumerate(nodes):
        for partner in nodes[c + 1:]:
            pairs.append([node, partner])

    return pairs

def get_distance(D, pairs):
    step_sum = 0
    for pair in pairs:
        # start, goal
        [x1, y1], [x2, y2] = pair

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        step_sum += dx+dy

    return step_sum


def get_distance_part2(D, pairs):
    step_sum = 0
    str = '*' * len(D[0])
    for pair in pairs:
        # start, goal
        [x1, y1], [x2, y2] = pair

        rows = D[min(x1,x2):max(x1,x2)]
        star_row_count = D[min(x1,x2):max(x1,x2)].count(str)
        dx = abs(x2 - x1)-star_row_count + star_row_count * (1000000-1)
        colums = D[0][min(y1,y2):max(y1,y2)]
        star_column_count = D[0][min(y1,y2):max(y1,y2)].count('*')
        dy = abs(y2 - y1)-star_column_count + star_column_count * (1000000-1)

        step_sum += dx+dy

    return step_sum

# get data
with open('11.in', 'r') as f:
    D = f.read().strip().split('\n')
print('input: ', D)


# Find rows & cols with only dots
rows_index_to_insert, column_index_to_insert = get_index(D)

# Insert expansion row
D = insert_space_row(D, rows_index_to_insert)
print('Rows expanded')
D = insert_space_col(D, column_index_to_insert)
print('Columns expanded\n')

# Find nodes
nodes = get_nodes(D)

# Identify pairs
pairs = get_pairs(nodes)
print('Unique pairs: ', len(pairs))


# Shortest path between node pairs
distance_sum = get_distance(D, pairs)
print('Total distance p1: ', distance_sum)

# Shortest path between node pairs
distance_sum = get_distance_part2(D, pairs)
print('Total distance p2: ', distance_sum)