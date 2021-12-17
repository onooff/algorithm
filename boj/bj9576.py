import sys

inputs = sys.stdin.readlines()
t = int(inputs[0])
idx = 1

for _ in range(t):
    ans = 0
    n, m = map(int, inputs[idx].rstrip().split())
    idx += 1
    books = {i for i in range(1, n + 1)}
    borrowers = list()
    for _ in range(m):
        borrowers.append(tuple(map(int, inputs[idx].rstrip().split())))
        idx += 1
    borrowers.sort(key=lambda x: x[1])
    for b in borrowers:
        if len(books) == 0:
            break
        for i in range(b[0], b[1] + 1):
            if i in books:
                books.discard(i)
                ans += 1
                break
    sys.stdout.write(f"{ans}\n")
