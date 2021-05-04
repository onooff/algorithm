def solution(n, path, order):
    answer = True
    road = dict()
    rooms = set([i for i in range(n)])
    # print(rooms)
    for p in path:
        if p[0] not in road:
            road.setdefault(p[0], list())
        if p[1] not in road:
            road.setdefault(p[1], list())
        road[p[0]].append(p[1])
        road[p[1]].append(p[0])
    # print(road)
    locked = dict()
    key = dict()
    for i in range(n):
        locked.setdefault(i, set())
        key.setdefault(i, set())
    for o in order:
        locked[o[1]].add(o[0])
        key[o[0]].add(o[1])

    if len(locked[0]) > 0:
        return False

    q = list()
    q.append(0)
    rooms.discard(0)
    locked_set = set()
    while len(q) > 0:
        now = q.pop(0)
        for open_room in list(key[now]):
            locked[open_room].discard(now)
            if (len(locked[open_room]) == 0) and (open_room in locked_set):
                q.append(open_room)
                rooms.discard(open_room)
                locked_set.discard(open_room)

        for next_room in road[now]:
            if next_room in rooms:
                if len(locked[next_room]) == 0:
                    q.append(next_room)
                    rooms.discard(next_room)
                else:
                    locked_set.add(next_room)

    if len(rooms) > 0:
        answer = False
    return answer
