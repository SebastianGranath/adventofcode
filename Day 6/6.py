with open('6.in','r') as f:
    D = f.read().strip()
L = D.split('\n')

T = [int(x) for x in L[0].split(':')[1].strip().split()]
D = [int(x) for x in L[1].split(':')[1].strip().split()]
print(T,D)


def f_travel(T, h):
    travel = (T - h) * h
    return travel
def calc_all(T, D):
    p1 = []
    p1_temp = 0
    dist = 0
    for nr, t in enumerate(T):
        for h in range(t):
            p_dist = dist
            dist = f_travel(t, h)
            if dist > D[nr]:
                p1_temp += 1
        if p1_temp > 0:
            p1.append(p1_temp)
            p1_temp = 0

    return p1

def calc_one(T,D):
    p2 = []
    p_temp = 0
    dist = 0

    srt = 0  # First element that we beat record with
    ed = 0   # Last element that we beat record with

    for h in range(0, T):
        p_dist = dist
        dist = f_travel(T, h)
        if dist > D:
            srt = h
            break
    for h in range(0, T):
        h = T - h  # Reverse search
        p_dist = dist
        dist = f_travel(T, h)
        if dist > D:
            ed = h
            break
    p2 = ed - srt + 1
    return p2



p1 = calc_all(T, D)
p1_fin = 0
for el in p1:
    if p1_fin == 0:
        p1_fin += el
    else:
        p1_fin *= el

print(p1_fin)

p2 = []

T = int(''.join(map(str, T)))
D = int(''.join(map(str, D)))
p2 = calc_one(T, D)
print(p2)

