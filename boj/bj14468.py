s = list(input())
answer = set()
for i in range(ord("A"), ord("Z") + 1):
    ch = chr(i)
    r = []
    for i in range(len(s)):
        if s[i] == ch:
            r.append(i)
            if len(r) == 2:
                break
    chk = set()
    for i in range(r[0] + 1, r[1]):
        if s[i] in chk:
            chk.discard(s[i])
        else:
            chk.add(s[i])
    for c in chk:
        answer.add(tuple(sorted([ch, c])))
print(len(answer))
