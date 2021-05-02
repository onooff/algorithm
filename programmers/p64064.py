d = dict()
keys = list()
ans = set()


def go(now=0, ban_set=set()):
    global d, keys, ans
    if now == len(keys):
        tmp = list(ban_set)
        tmp.sort()
        ans.add(tuple(tmp))
        return

    l = d[keys[now]]
    for bid in l:
        if bid not in ban_set:
            ban_set.add(bid)
            go(now+1, ban_set)
            ban_set.discard(bid)
    return


def solution(user_id, banned_id):
    global d, keys, ans
    idx = 0
    for bid in banned_id:
        tmp = list()
        for uid in user_id:
            if len(bid) == len(uid):
                is_ban = True
                for i in range(len(bid)):
                    if bid[i] == '*':
                        continue
                    if bid[i] != uid[i]:
                        is_ban = False
                        break
                if is_ban:
                    tmp.append(uid)
        d.setdefault(idx, tmp)
        idx += 1
    keys = list(d.keys())
    print(d)
    go(0, set())
    return len(ans)
