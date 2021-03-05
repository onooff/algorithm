t = int(input())

for tc in range(t):
    n, u, v = map(int, input().split())
    a = list(map(int, input().split()))
    last = a[0]
    ans = min(v+v, v+u)
    for i in range(n):
        if abs(last-a[i]) > 1:
            ans = 0
            break
        elif last != a[i]:
            ans = min(u, v)
        last = a[i]
    print(ans)
