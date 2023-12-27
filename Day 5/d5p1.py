#  destination range start, the source range start, and the range length
with open('d5input.txt', 'r') as f:
    data = f.readlines()

seed_nr = data.pop(0).strip().split(':')[1].strip().split(' ')

dest_source = []
for line in data:
    try:
        dest_source.append([range(2)])
    except:
        pass
seed2soil = 0



print(data)