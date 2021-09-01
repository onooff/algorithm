c = ['A', 'E', 'I', 'O', 'U']
cnt = 0
end = False


def dfs(s, w):
    global c, cnt, end
    if end:
        return
    for cc in c:
        new = s+cc
        cnt += 1
        if new == w:
            end = True
            return
        if len(new) < 5:
            dfs(new, w)
            if end:
                return


def solution(word):
    global cnt
    dfs('', word)
    return cnt
