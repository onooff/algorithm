def solution1(words, queries):
    answer = [0 for i in range(len(queries))]
    qd = dict()
    for idx in range(len(queries)):
        q = queries[idx]
        l = len(q)
        last = len(q)-1
        qd.setdefault(l, {0: dict(), 1: dict()})
        s = 0
        e = l
        if q[0] == '?':
            for i in range(0, l):
                if q[i] != '?':
                    e = i
                    break
            cnt = e-s
            tmp = q[e:]
            qd[l][0].setdefault(cnt, dict())
            qd[l][0][cnt].setdefault(tmp, list())
            qd[l][0][cnt][tmp].append(idx)
        elif q[last] == '?':
            for i in range(last, -1, -1):
                if q[i] != '?':
                    s = i+1
                    break
            cnt = e-s
            tmp = q[:s]
            qd[l][1].setdefault(cnt, dict())
            qd[l][1][cnt].setdefault(tmp, list())
            qd[l][1][cnt][tmp].append(idx)
    for w in words:
        l = len(w)
        if l in qd:
            for i in range(1, l+1):
                if i in qd[l][0]:
                    test = w[i:]
                    if test in qd[l][0][i]:
                        answer[qd[l][0][i][test][0]] += 1
                        # for gogo in qd[l][0][i][test]:
                        #     answer[gogo]+=1
                if i in qd[l][1]:
                    test = w[:l-i]
                    if test in qd[l][1][i]:
                        answer[qd[l][1][i][test][0]] += 1
                        # for gogo in qd[l][1][i][test]:
                        #     answer[gogo]+=1
    for q1 in qd:
        for q2 in qd[q1]:
            for q3 in qd[q1][q2]:
                for q4 in qd[q1][q2][q3]:
                    tmp = qd[q1][q2][q3][q4]
                    if len(tmp) > 1:
                        for i in range(1, len(tmp)):
                            answer[tmp[i]] = answer[tmp[0]]

    return answer


def solution2(words, queries):
    answer = []
    trie = dict()
    trie_rev = dict()
    for w in words:
        l = len(w)
        trie.setdefault(l, [dict(), 0])
        trie_rev.setdefault(l, [dict(), 0])
        trie[l][1] += 1
        trie_rev[l][1] += 1
        nowt = trie[l][0]
        nowtr = trie_rev[l][0]
        for i in range(len(w)):
            c = w[i]
            rc = w[len(w)-1-i]
            nowt.setdefault(c, [dict(), 0])
            nowtr.setdefault(rc, [dict(), 0])
            nowt[c][1] += 1
            nowtr[rc][1] += 1
            nowt = nowt[c][0]
            nowtr = nowtr[rc][0]
    # print(trie)
    # print(trie_rev)
    for q in queries:
        l = len(q)
        flag = True
        if l not in trie:
            answer.append(0)
            continue
        if q[0] == '?' and q[l-1] == '?':
            answer.append(trie[l][1])
        elif q[0] != '?':
            idx = 0
            go = trie[l][0]
            while q[idx+1] != '?':
                if q[idx] not in go:
                    flag = False
                    break
                go = go[q[idx]][0]
                idx += 1
            if flag and q[idx] in go:
                answer.append(go[q[idx]][1])
            else:
                answer.append(0)
        elif q[l-1] != '?':
            idx = l-1
            go = trie_rev[l][0]
            while q[idx-1] != '?':
                if q[idx] not in go:
                    flag = False
                    break
                go = go[q[idx]][0]
                idx -= 1
            if flag and q[idx] in go:
                answer.append(go[q[idx]][1])
            else:
                answer.append(0)
    return answer


print(solution2(["frodo", "front", "frost", "frozen", "frame",
                 "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
