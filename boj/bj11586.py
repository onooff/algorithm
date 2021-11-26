mirror = list()
n = int(input())
for _ in range(n):
    mirror.append(list(input()))
status = int(input())

if status == 2:
    for i in range(n):
        mirror[i].reverse()
elif status == 3:
    mirror.reverse()

for i in range(n):
    print(''.join(mirror[i]))
