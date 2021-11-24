import sys
l = sys.stdin.readlines()
l.pop(0)
for i in range(len(l)):
    l[i] = l[i].rstrip().split()
    l[i][1:] = list(map(int, l[i][1:]))

l.sort(key=lambda x: (x[3], x[2], x[1]))
print(l[-1][0], l[0][0], sep='\n')
