n = int(input())

s = input()

ans = 0
idx = 0
ppap = ['p', 'P', 'A', 'p']
for i in range(n):
    if s[i] == ppap[idx]:
        if idx == 3:
            ans += 1
            idx = 0
        else:
            idx += 1
    else:
        if s[i] == 'p':
            idx = 1
        else:
            idx = 0
print(ans)
