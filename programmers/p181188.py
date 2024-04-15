def solution(targets):
    targets = [(i, t[0], t[1] - 1) for i, t in enumerate(targets)]
    dict_targets = {t[0]: t for t in targets}
    order_by_start = sorted([t[0] for t in targets], key=lambda x: dict_targets[x][1])
    order_by_end = sorted([t[0] for t in targets], key=lambda x: dict_targets[x][2])
    idxs = set(dict_targets.keys())
    cur = 0
    answer = 0
    for i in order_by_end:
        if i in idxs:
            answer += 1
            while (
                cur < len(order_by_start)
                and dict_targets[order_by_start[cur]][1] <= dict_targets[i][2]
            ):
                idxs.discard(order_by_start[cur])
                cur += 1
        if len(idxs) == 0:
            break
    return answer
