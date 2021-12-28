input()
l = list(map(int, input().split()))
l.sort()
test = [-1 for _ in range(len(l) * 2)]
chk = set()


def dfs(l, test, chk, cur):
    if cur == len(test):
        if len(chk) == len(l):
            return True
        else:
            return False
    for num in l:
        if num in chk:
            continue
        pair = cur + num + 1
        if pair < len(test) and test[pair] == -1:
            chk.add(num)
            test[cur], test[pair] = num, num
            nxt = cur + 1
            while nxt < len(test) and test[nxt] != -1:
                nxt += 1
            ret = dfs(l, test, chk, nxt)
            if ret:
                return ret
            test[cur], test[pair] = -1, -1
            chk.discard(num)
    return False


is_ans = dfs(l, test, chk, 0)
if is_ans:
    for num in test:
        print(num, end=" ")
else:
    print(-1)
