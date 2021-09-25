import sys
inputs = sys.stdin.readlines()

t = int(inputs[0])
idx = 1
for _ in range(t):
    n = int(inputs[idx])
    idx += 1
    l = list(map(int, inputs[idx].rstrip().split()))
    idx += 1

    ans = 0
    chk = {i for i in range(1, n+1)}
    for i in range(len(l)):
        start = i+1
        if start not in chk:
            continue
        go = start
        chk_tmp = {go}
        chk_tmp_l = [go]
        while l[go-1] not in chk_tmp and l[go-1] in chk:
            go = l[go-1]
            chk_tmp.add(go)
            chk_tmp_l.append(go)
        if l[go-1] not in chk:
            for n in chk_tmp_l:
                chk.discard(n)
                ans += 1
        else:
            team_start = l[go-1]
            ts_idx = chk_tmp_l.index(team_start)
            for n in chk_tmp_l[:ts_idx]:
                chk.discard(n)
                ans += 1
            for n in chk_tmp_l[ts_idx:]:
                chk.discard(n)
    print(ans)
