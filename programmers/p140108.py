def solution(s):
    ans = 0
    first = False
    cnt = 0
    for i, c in enumerate(s):
        if not first:
            ans += 1
            first = c
            cnt = 1
        else:
            if c == first:
                cnt += 1
            else:
                cnt -= 1
        if cnt == 0:
            first = False

    return ans
