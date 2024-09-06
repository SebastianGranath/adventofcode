import sys
import re
with open('11.test', 'r') as f:
    D = f.read().strip().split('\n')
print('input: ', D)

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
        D.insert(el+i_count, D[rows_index_to_insert[0]])
        i_count += 1
    return D

def insert_space_col(D, column_index_to_insert):
    i_count = 0
    for i, el in enumerate(column_index_to_insert):
        for r, row in enumerate(D):

            D[r] = D[r][:el+i_count] + '.' + D[r][el+i_count:]
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
# Find rows & cols with only dots
rows_index_to_insert, column_index_to_insert = get_index(D)

# Insert expansion row
D = insert_space_row(D, rows_index_to_insert)
print('Rows expand\n', D)
D = insert_space_col(D, column_index_to_insert)
print('columns expand\n', D)

# Find nodes
nodes = get_nodes(D)

# Identify pairs
pairs = get_pairs(nodes)
print('Unique pairs: ', len(pairs))


# Shortest path between node pairs
for pair in pairs:
    [x1, y1], [x2, y2] = pair
    x, y = x1, y1
    dx = x2-x1
    dy = y2-y1
    if dx == 0: dx = 0.1
    gradient = dy / float(dx)
    print(gradient)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x

        x1, y1 = y1, x1
        x2, y2 = y2, x2
        p = 2*dy - dx
        print(f"x = {x}, y = {y}")
        # Initialize the plotting points
        xcoordinates = [x]
        ycoordinates = [y]

        for k in range(2, dx + 2):
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy

            x = x + 1 if x < x2 else x - 1

            print(f"x = {x}, y = {y}")
            xcoordinates.append(x)
            ycoordinates.append(y)
    print(pair,' got steps ', len(xcoordinates)-1)

# n - nodes
# Pairs = sum(n - 1) n->1
# Bresenheims line algorithm
