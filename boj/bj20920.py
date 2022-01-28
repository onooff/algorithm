import sys
inputs = sys.stdin.readlines()
d = dict()
n, m = map(int, inputs[0].split())
for i in range(1, len(inputs)):
    word = inputs[i].rstrip()
    if len(word) >= m:
        d.setdefault(word, 0)
        d[word] += 1

ans = list(d.keys())
ans.sort(key=lambda x: (-d[x], -len(x), x))
print('\n'.join(ans))
