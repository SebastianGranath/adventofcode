with open('output.txt', 'r') as f:
    dat = f.readlines()
a = dat[1]
a = dat[1][1:-2]
a = a.split(',')

b = dat[2]
b = dat[2][1:-2]
b = b.split(',')
print(set(a) ^ set(b))