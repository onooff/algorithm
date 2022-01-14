seat = set()
input()
order = list(map(int, input().split()))
ans = 0
for o in order:
    if o in seat:
        ans += 1
    else:
        seat.add(o)
print(ans)
