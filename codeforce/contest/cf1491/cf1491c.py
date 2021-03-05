t = int(input())

for tc in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    ss = [0 for i in range(n)]
    for i in range(n):
        next_val = i+s[i]
        while True:
            if next_val >= n:
                break
            ss[next_val] += 1
            next_val += s[next_val]
    m = min(ss)
    for i in range(n):
        if s[i] != 1 and ss[i] == m:
            pass
    print(s, ss)
