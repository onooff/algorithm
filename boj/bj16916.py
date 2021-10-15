s = input()
p = input()
kmp = [0 for _ in range(len(p))]
j = 0
for i in range(1, len(p)):
    while j > 0 and p[i] != p[j]:
        j = kmp[j-1]
    if p[i] == p[j]:
        j += 1
        kmp[i] = j

j = 0
ans = 0
for i in range(len(s)):
    while j > 0 and s[i] != p[j]:
        j = kmp[j-1]
    if s[i] == p[j]:
        if j == len(p)-1:
            ans = 1
        else:
            j += 1
    if ans > 0:
        break
print(ans)
