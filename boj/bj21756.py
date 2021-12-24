n = int(input())
l = [i for i in range(1, n + 1)]
while len(l) > 1:
    l = [l[i] for i in range(1, len(l), 2)]
print(l[0])
