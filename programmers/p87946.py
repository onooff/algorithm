answer = 0


def dfs(remain, dungeons, chk, not_chked):
    global answer
    end = True
    if not_chked > 0:
        for i in range(len(dungeons)):
            if not chk[i] and dungeons[i][0] <= remain:
                end = False
                chk[i] = True
                dfs(remain-dungeons[i][1], dungeons, chk, not_chked-1)
                chk[i] = False
                if answer == len(dungeons):
                    return
    if end:
        answer = max(answer, len(dungeons)-not_chked)


def solution(k, dungeons):
    global answer
    chk = [False for i in range(len(dungeons))]
    dfs(k, dungeons, chk, len(dungeons))
    return answer
