import sys
inputs = sys.stdin.readlines()

data = list()
for i in range(1, len(inputs)):
    tmp = inputs[i].split()
    tmp[1] = int(tmp[1])
    tmp[2] = int(tmp[2])
    tmp[3] = int(tmp[3])
    data.append(tmp)

data.sort(key=lambda x: x[0])
data.sort(key=lambda x: -x[3])
data.sort(key=lambda x: x[2])
data.sort(key=lambda x: -x[1])

for d in data:
    sys.stdout.write(d[0]+'\n')
