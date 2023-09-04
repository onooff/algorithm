import sys

inputs = sys.stdin.readlines()
answer = list()

for i in range(1, len(inputs)):
    s = inputs[i].rstrip()
    a = 0
    for c in s:
        a += int(c)
    b = int(s[-3:]) * 10
    ans = a + b
    if ans < 1000:
        ans += 1000
    answer.append(str(ans)[-4:])

print(*answer, sep="\n")
