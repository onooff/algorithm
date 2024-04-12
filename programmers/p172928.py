def solution(park, routes):
    d = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
    h = len(park)
    w = len(park[0])

    y = -1
    x = -1
    for i, row in enumerate(park):
        if "S" in row:
            y = i
            x = row.index("S")
            break

    for r in routes:
        op, n = r.split()
        n = int(n)
        ny = y
        nx = x
        is_ok = True
        for _ in range(n):
            ny += d[op][0]
            nx += d[op][1]
            if not (0 <= ny < h and 0 <= nx < w and park[ny][nx] != "X"):
                is_ok = False
                break
        if is_ok:
            y = ny
            x = nx

    return [y, x]
