dic = {
    "000000": "A",
    "001111": "B",
    "010011": "C",
    "011100": "D",
    "100110": "E",
    "101001": "F",
    "110101": "G",
    "111010": "H",
}

inverse = {"1": "0", "0": "1"}

keys = list(dic.keys())
for k in keys:
    c = dic[k]
    k = list(k)
    for i in range(len(k)):
        k[i] = inverse[k[i]]
        dic.setdefault("".join(k), c)
        k[i] = inverse[k[i]]

input()
s = input()
ans = list()
for i in range(0, len(s), 6):
    chk = s[i : i + 6]
    if chk not in dic:
        ans = i // 6 + 1
        break
    ans.append(dic[chk])

if type(ans) == type(list()):
    print("".join(ans))
else:
    print(ans)
