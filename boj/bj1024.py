n, l = map(int, input().split())

chk = 0
for i in range(l):
    chk += i
while True:
    if (n-chk) % l == 0 or n-chk < 0 or l > 100:
        break

    i += 1
    chk += i
    l += 1
    # print(l, i)

# print(l, i)
if n-chk < 0 or l > 100:
    print(-1)
else:
    start = (n-chk)//l
    for i in range(l):
        print(start+i, end=' ')
