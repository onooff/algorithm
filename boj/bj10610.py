l = list(map(int, list(input())))
if 0 in l and sum(l) % 3 == 0:
    l.sort(key=lambda x: -x)
    print(''.join(map(str, l)))
else:
    print(-1)
