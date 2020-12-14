t = int(input())
for tc in range(1, t+1):
    ans = 0

    input()
    s = list(map(int, input().split()))
    s.sort()

    now = s[0]
    count = 1
    maxCount = 0
    for i in range(1, len(s)):
        if s[i] != now:
            if count >= maxCount:
                ans = now
                maxCount = count
            now = s[i]
            count = 1
        else:
            count += 1

    print('#', tc, ' ', ans, sep='')
