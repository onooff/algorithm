t = int(input())
for _ in range(t):
    sett = {i for i in range(65, 91)}
    s = input()
    for c in s:
        sett.discard(ord(c))
    print(sum(sett))
