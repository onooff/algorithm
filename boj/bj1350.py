n = int(input())
files = list(map(int, input().split()))
unit = int(input())

ans = 0
for f in files:
    if f % unit == 0:
        ans += f
    else:
        ans += ((f//unit)+1)*unit
print(ans)
