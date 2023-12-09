import numpy as np
with open('day2input.txt', 'r') as f:
    data = f.readlines()

answer = 0
colors = ['red', 'green', 'blue']
lims = [12, 13, 14]
for line in data:
    line = line.split(':')
    id = line[0].split(' ')[-1]
    games = line[1].split(';')
    results = np.zeros((len(games), 3))

    for i in range(len(games)):
        for j in range(len(colors)):
            try:
                # ERRORS IN THIS SECTION, missing out 20 -> only taking 0
                results[i][j] = games[i][games[i].index(colors[j])-2]
                temp = games[i].replace(',', '').split(' ')
                for word in temp:
                    temp2 = word.split(' ')
                    print(temp2.index(colors[j]))
                    print(word.index(colors[j]))
                results[i][j] = temp[temp.index(colors[j]) - 1]
            except:
                results[i][j] = 0
    print('Continue here')

    if ( (results[:,0] <= lims[0]).all() and (results[:,1] <= lims[1]).all() and (results[:,2]<= lims[2]).all()):
        answer = answer + int(id)

print(answer)

