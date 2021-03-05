import math
t = int(input())

for tc in range(t):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    ans1 = 0
    ans2 = 0
    for n in l:
        ans1 += n
        ans2 += math.ceil(n/x)
    print(math.ceil(ans1/x), ans2)
