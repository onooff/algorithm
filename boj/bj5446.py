import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n1 = int(input())
    del_files = dict()
    for _ in range(n1):
        del_file = input().rstrip()
        cur = del_files
        for c in del_file:
            cur.setdefault(c, [dict(), 0])
            cur[c][1] += 1
            cur = cur[c][0]
        cur.setdefault("end", 0)
        cur["end"] += 1

    n2 = int(input())
    not_del_files = dict()
    for _ in range(n2):
        not_del_file = input().rstrip()
        cur = not_del_files
        for c in not_del_file:
            cur.setdefault(c, [dict(), 0])
            cur[c][1] += 1
            cur = cur[c][0]
        cur.setdefault("end", 0)
        cur["end"] += 1

    if n2 == 0:
        print(1)
        continue

    answer = 0
    q = list()
    for start in del_files:
        if del_files[start][1] == 1 or start not in not_del_files:
            answer += 1
        else:
            q.append((del_files[start], not_del_files[start]))

    idx = 0
    while idx < len(q):
        tmp = q[idx]
        idx += 1
        cur = tmp[0]
        chk = tmp[1]

        d = cur[0]
        n = cur[1]
        chk_d = chk[0]
        chk_n = chk[1]
        for nxt in d:
            if nxt == "end":
                answer += 1
                continue

            if nxt in chk_d and d[nxt][1] > 1:
                q.append((d[nxt], chk_d[nxt]))
            else:
                answer += 1
    print(answer)
