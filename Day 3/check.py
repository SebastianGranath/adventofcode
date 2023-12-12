with open('output.txt', 'r') as f:
    dat = f.readlines()
a = dat[1].split(',')
a = [eval(i) for i in a]
b = dat[2]
print(set(a) & set(b))