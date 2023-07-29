s = list(input())

cnt = [0, 0]
for c in s:
    if c == "0":
        cnt[0] += 0.5
    elif c == "1":
        cnt[1] += 0.5


for i in range(len(s)):
    if s[i] == "1":
        s[i] = ""
        cnt[1] -= 1
        if cnt[1] == 0:
            break

for i in range(len(s) - 1, -1, -1):
    if s[i] == "0":
        s[i] = ""
        cnt[0] -= 1
        if cnt[0] == 0:
            break

print("".join(s))
