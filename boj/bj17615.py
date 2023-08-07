input()
s = input()

l = list()
last = None
cnt = 0
r_sum = 0
b_sum = 0
for c in s:
    if last != c:
        l.append((last, cnt))
        if last == "R":
            r_sum += cnt
        elif last == "B":
            b_sum += cnt
        last = c
        cnt = 1
    else:
        cnt += 1

l.append((last, cnt))
if last == "R":
    r_sum += cnt
elif last == "B":
    b_sum += cnt
l.pop(0)

ans = float("inf")
if l[0][0] == "R" and l[-1][0] == "R":
    ans = min(ans, r_sum - max(l[0][1], l[-1][1]))
elif l[0][0] != "R" and l[-1][0] != "R":
    ans = min(ans, r_sum)
else:
    ans = min(ans, r_sum - (l[0][1] if l[0][0] == "R" else l[-1][1]))

if l[0][0] == "B" and l[-1][0] == "B":
    ans = min(ans, b_sum - max(l[0][1], l[-1][1]))
elif l[0][0] != "B" and l[-1][0] != "B":
    ans = min(ans, b_sum)
else:
    ans = min(ans, b_sum - (l[0][1] if l[0][0] == "B" else l[-1][1]))

print(ans)
