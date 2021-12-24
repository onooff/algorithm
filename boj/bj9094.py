import sys

inputs = sys.stdin.readlines()

for i in range(1, len(inputs)):
    n, m = map(int, inputs[i].rstrip().split())
    cnt = 0
    sq = [tmp ** 2 for tmp in range(n)]
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if (sq[a] + sq[b] + m) % (a * b) == 0:
                cnt += 1
    sys.stdout.write(f"{cnt}\n")
