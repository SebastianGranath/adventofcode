import numpy as np
with open('day2input.txt', 'r') as f:
    data = f.readlines()


colors = [' red', ' green', ' blue']
lims = [6, 5, 4]
for line in data:
    line = line.split(':')
    id = line[0].split(' ')[-1]
    games = line[1].split(';')
    results = np.zeros((3, len(games)))

    for i in range(len(games)):
        for j in range(len(colors)):
            try:
                # ERRORS IN THIS SECTION
                results[j][i] = games[i][games[i].index(colors[j])-1]
                print(results[j][i])
            except:
                results[j][i] = 0


        print(games[i])
    try:
        print(id)
    except:
        pass
