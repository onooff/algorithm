import sys
inputs = sys.stdin.readlines()

trie = dict()
names = dict()
for i in range(1, len(inputs)):
    cur = trie
    name = inputs[i].rstrip()
    if name in names:
        names[name] += 1
        print(name, names[name], sep='')
        continue
    names.setdefault(name, 1)
    cut = 0
    flag = True
    for c in name:
        if flag:
            cut += 1
            if c not in cur:
                flag = False
        cur.setdefault(c, dict())
        cur = cur[c]
    print(name[:cut])
