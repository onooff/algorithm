import sys
inputs = sys.stdin.readlines()
n, m = map(int, inputs[0].split())
books = list()
idx = 2
top = dict()
for i in range(m):
    books.append(list(map(int, inputs[idx].split())))
    top.setdefault(books[i][len(books[i])-1], i)
    idx += 2

is_ok = True
for i in range(1, n+1):
    if i not in top:
        is_ok = False
        break
    stk_idx = top[i]
    top.pop(i)
    books[stk_idx].pop()
    if len(books[stk_idx]) > 0:
        top.setdefault(books[stk_idx][len(books[stk_idx])-1], stk_idx)

if is_ok:
    print("Yes")
else:
    print("No")
