t = int(input())

chk = set()
for i in range(1, 10001):
    chk.add((i**3))

for tc in range(t):
    n = int(input())
    is_yes = False
    for num in chk:
        if n-num in chk:
            is_yes = True
            break
    if is_yes:
        print('yes')
    else:
        print('no')
