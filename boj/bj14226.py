lim = 1000
s = int(input())
pq = [(0, 1, 0)]  # time, len, cliplen
idx = 0
chk = {1: {0}}
while len(pq) > 0:
    t, l, cl = pq[idx]
    idx += 1
    # print(t, l, cl)
    if l == s:
        print(t)
        break
    t += 1

    if l not in chk[l]:
        pq.append((t, l, l))
        chk[l].add(l)

    nl = l + cl
    if nl <= lim and (nl not in chk or cl not in chk[nl]):
        pq.append((t, nl, cl))
        chk.setdefault(nl, set())
        chk[nl].add(cl)

    nl = l - 1
    if nl > 0 and (nl not in chk or cl not in chk[nl]):
        pq.append((t, nl, cl))
        chk.setdefault(nl, set())
        chk[nl].add(cl)
