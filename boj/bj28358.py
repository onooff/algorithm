import sys

days = list()
ed = (
    0,
    31,
    29,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
)
for m in range(1, 13):
    for d in range(1, ed[m] + 1):
        days.append(set(str(m) + str(d)))

inputs = sys.stdin.readlines()
answer = list()
for i in range(1, len(inputs)):
    chk = set()
    l = inputs[i].rstrip().split()
    for j in range(len(l)):
        if l[j] == "1":
            chk.add(str(j))
    cnt = 366
    for day in days:
        if chk & day:
            cnt -= 1
    answer.append(cnt)
print(*answer, sep="\n")
