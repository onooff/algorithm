n = int(input())
l = list(map(int, input().split()))

left, right = 0, 0
d = {l[0]: 1}

while right + 1 < n:
    right += 1
    d.setdefault(l[right], 0)
    d[l[right]] += 1
    if len(d) >= 3:
        d[l[left]] -= 1
        if d[l[left]] == 0:
            d.pop(l[left])
        left += 1

print(right - left + 1)
