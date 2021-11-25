import sys


def is_pal(s, l, r, result):
    while l < r:
        if s[l] != s[r]:
            if result == 0:
                result += 1
                if s[l+1] == s[r] and s[l] == s[r-1]:
                    return min(is_pal(s, l+1, r, result), is_pal(s, l, r-1, result))
                elif s[l+1] == s[r]:
                    l += 1
                elif s[l] == s[r-1]:
                    r -= 1
                else:
                    return 2
                continue
            else:
                return 2
        l += 1
        r -= 1
    return result


inputs = sys.stdin.readlines()
for i in range(1, len(inputs)):
    s = inputs[i].rstrip()
    print(is_pal(s, 0, len(s)-1, 0))
