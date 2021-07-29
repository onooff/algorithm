min_cnt = 999999999999999


def dfs(s, n, bset, num):
    global min_cnt
    if len(s) > 0:
        sn = int(s)
        chk = max(sn, num)-min(sn, num)+len(s)
        min_cnt = min(min_cnt, chk)
        # print(min_cnt, s)
    if s == '0' or len(s) == n:
        return
    for b in bset:
        dfs(s+b, n, bset, num)


n = int(input())
m = int(input())
if m == 0:
    print(min(len(str(n)), (max(100, n)-min(100, n))))
elif m == 10:
    print(max(100, n)-min(100, n))
else:
    button_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    broken_buttons = list(input().split())
    for b in broken_buttons:
        button_set.discard(b)
    min_cnt = max(100, n)-min(100, n)
    dfs("", len(str(n))+1, button_set, n)
    print(min_cnt)
