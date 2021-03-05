n, q = map(int, input().split())

a = list(map(int, input().split()))
count = [0, 0]
for num in a:
    count[num] += 1
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        x -= 1
        count[a[x]] -= 1
        a[x] = 1-a[x]
        count[a[x]] += 1
    else:
        if x <= count[1]:
            print(1)
        else:
            print(0)
