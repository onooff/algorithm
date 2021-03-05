import math
t = int(input())

for tc in range(t):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    ans1 = math.ceil(sum(list)/3)
    ans2 = 0
    for n in list:
        ans2 += math.ceil(n/x)
    print(ans1, ans2)
