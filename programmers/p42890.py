import itertools

d = dict()
chk = list()


def sub(now=0, tc=0):
    global d, chk
    if now == len(chk):
        d.setdefault(tuple(chk+[tc]), set())
        return
    for i in [False, True]:
        chk[now] = i
        if i:
            sub(now+1, tc+1)
        else:
            sub(now+1, tc)


def solution(relation):
    global d, chk
    answer = 0
    chk = [False for i in range(len(relation[0]))]
    sub(0)
    # print(d)
    chk = list()

    for k in d:
        for r in relation:
            tmp = list()
            for i in range(len(k)-1):
                if k[i] == True:
                    tmp.append(r[i])
            d[k].add(tuple(tmp))
    key = list(d.keys())
    key.sort(key=lambda x: x[len(x)-1])
    # aa = 0
    for k in key:
        minimal = True
        # if len(relation) == len(d[k]):
        #     aa += 1
        for ci in range(len(chk)):
            cnt = 0
            for i in range(len(chk[ci])-1):
                if chk[ci][i] and k[i]:
                    cnt += 1
            # print('>>>>>>>', cnt, chk[ci][len(chk[ci])-1])
            if cnt == chk[ci][len(chk[ci])-1]:
                minimal = False
                break
        if not minimal:
            continue
        else:
            # print(len(d[k]), k)
            if len(relation) == len(d[k]):
                answer += 1
                # for i in range(len(chk)):
                #     if k[i]:
                #         chk[i] = True
                chk.append(k[:len(k)])
                # print('>>>', answer, chk)
    # for k in d:
    #     print(k, len(d[k]), d[k])
    # print(aa)
    return answer


print(solution(	[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
      "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
