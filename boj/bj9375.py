t = int(input())
for tc in range(t):
    wear = dict()
    n = int(input())
    for i in range(n):
        a, b = input().split()
        if b not in wear.keys():
            wear.setdefault(b, set())
        wear[b].add(a)
    ans = 1
    for k in wear.keys():
        ans *= (len(wear[k])+1)
    print(ans-1)
