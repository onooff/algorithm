l = int(input())
li = list(map(int, input().split()))
n = int(input())

li.sort()

left = -1
right = -1

for i in range(l):
    if li[i] == n:
        break
    if li[i] > n:
        if i == 0:
            left = 0
        else:
            left = li[i - 1]
        right = li[i]
        break

if left == -1 and right == -1:
    print(0)
else:
    print((n - left) * (right - n) - 1)
