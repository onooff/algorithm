def is_in(y=0, x=0):
    return 0 <= y < 5 and 0 <= x < 5


def solution(places):
    answer = list()
    d0 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    d1 = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    d2 = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
    for p_idx in range(len(places)):
        answer.append(1)
        p = places[p_idx]
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    for d in range(4):
                        ni = i+d0[d][0]
                        nj = j+d0[d][1]
                        if is_in(ni, nj) and p[ni][nj] == 'P':
                            answer[p_idx] = 0
                            break
                    if answer[p_idx] == 0:
                        break
                    for d in range(4):
                        ni = i+d1[d][0]
                        nj = j+d1[d][1]
                        if is_in(ni, nj) and p[ni][nj] == 'P':
                            if d == 0:
                                if p[i][j+1] != 'X':
                                    answer[p_idx] = 0
                            elif d == 1:
                                if p[i][j-1] != 'X':
                                    answer[p_idx] = 0
                            elif d == 2:
                                if p[i+1][j] != 'X':
                                    answer[p_idx] = 0
                            elif d == 3:
                                if p[i-1][j] != 'X':
                                    answer[p_idx] = 0
                        if answer[p_idx] == 0:
                            break
                    # d2=[(1,1),(-1,-1),(-1,1),(1,-1)]
                    if answer[p_idx] == 0:
                        break
                    for d in range(4):
                        ni = i+d2[d][0]
                        nj = j+d2[d][1]
                        if is_in(ni, nj) and p[ni][nj] == 'P':
                            if not(p[ni][j] == 'X' and p[i][nj] == 'X'):
                                answer[p_idx] = 0
                                break
                    if answer[p_idx] == 0:
                        break
                if answer[p_idx] == 0:
                    break
            if answer[p_idx] == 0:
                break
        # print(p, answer[p_idx])
    return answer


# print(solution([[
#     "OOOOO",
#     "PXPOO",
#     "XOXOO",
#     "PXPOO",
#     "OOOOO"]]))
