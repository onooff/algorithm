n = int(input())
for _ in range(n):
    s = input().split()
    for i in range(len(s)):
        s[i] = list(s[i])
        s[i].reverse()
        s[i] = ''.join(s[i])
        print(s[i], end=' ')
    print()
