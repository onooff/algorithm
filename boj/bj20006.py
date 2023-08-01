import sys

input = sys.stdin.readline

p, m = map(int, input().split())

rooms = []
if m == 1:
    for _ in range(p):
        lv, name = input().split()
        rooms.append([False, lv, [(name, lv)]])

else:
    for _ in range(p):
        lv, name = input().split()
        lv = int(lv)
        is_join = False

        for r in rooms:
            if r[0] and r[1] - 10 <= lv <= r[1] + 10:
                is_join = True
                r[2].append((name, lv))
                if len(r[2]) == m:
                    r[0] = False
                break
        if not is_join:
            rooms.append([True, lv, [(name, lv)]])

for r in rooms:
    ans = []
    if r[0]:
        ans.append("Waiting!")
    else:
        ans.append("Started!")
    for member in sorted(r[2]):
        ans.append(f"{member[1]} {member[0]}")
    print("\n".join(ans))
