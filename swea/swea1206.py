for tc in range(1, 11):
    ans = 0
    n = int(input())
    b = list(map(int, input().split()))
    for i in range(n):
        if b[i] != 0:
            if b[i-1] < b[i] and b[i-2] < b[i] and b[i+1] < b[i] and b[i+2] < b[i]:
                ans += min(b[i]-b[i-1], b[i]-b[i-2], b[i]-b[i+1], b[i]-b[i+2])
    print('#', tc, ' ', ans, sep='')
