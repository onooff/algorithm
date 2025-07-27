a, b = map(int, input().split())


# commit test
def go(b, a, cnt):
    if b == a:
        return cnt
    if b % 10 == 1:
        return go((b - 1) // 10, a, cnt + 1)
    if b > 0 and b % 2 == 0:
        return go(b // 2, a, cnt + 1)
    return -1


print(go(b, a, 1))
