import sys

inputs = sys.stdin.readlines()
n, d, k, c = map(int, inputs[0].split())
l = [int(inputs[i]) for i in range(1, len(inputs))]

dic = dict()
dic.setdefault(c, 1)
for i in range(k):
    dic.setdefault(l[i], 0)
    dic[l[i]] += 1
ans = len(dic)

for i in range(k, len(l) + k):
    ii = i % len(l)

    discard = l[ii - k]
    dic[discard] -= 1
    if dic[discard] == 0:
        dic.pop(discard)

    dic.setdefault(l[ii], 0)
    dic[l[ii]] += 1

    if len(dic) > ans:
        ans = len(dic)

print(ans)
