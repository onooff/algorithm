s = input()

size = s.count("a")
cnt = s[:size].count("b")
ans = cnt
for i in range(1, len(s)):
    discard = i - 1
    if s[discard] == "b":
        cnt -= 1

    add = (i + size - 1) % len(s)
    if s[add] == "b":
        cnt += 1

    ans = min(ans, cnt)
print(ans)
