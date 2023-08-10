n = int(input())
l = list(map(int, input().split()))

head = [None, 1, l[0], None]
last = head
for i in range(1, n):
    new = [None, i + 1, l[i], None]
    last[3] = new
    new[0] = last
    last = new
last[3] = head
head[0] = last

ans = list()
cur = head
tmp = None
while True:
    ans.append(str(cur[1]))
    tmp = cur
    cur[0][3], cur[3][0] = cur[3], cur[0]
    if cur[2] > 0:
        for _ in range(cur[2]):
            tmp = tmp[3]
    else:
        for _ in range(-cur[2]):
            tmp = tmp[0]
    if cur is tmp:
        break
    cur = tmp

print(" ".join(ans))
