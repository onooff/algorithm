h, m = map(int, input().split(':'))
h %= 12
values = list(map(int, input().split()))
ans = sum(values)
n = int(input())
for _ in range(n):
    event = input().split()[1]
    d = 0
    if event[0] == '^':
        ans -= values[h//2]
        values[h//2] = 0
        if ans == 0:
            break
    elif event[0] == '1':
        d = 10
    elif event[0] == '3':
        d = 30
    elif event[0] == '5':
        d = 50
    elif event[0] == '2':
        d = 120
    elif event[0] == '4':
        d = 240
    elif event[0] == '9':
        d = 540
    if d > 0:
        m += d
        hh = m//60
        m %= 60
        h = (h+hh) % 12
if ans > 100:
    ans = 100
print(ans)
