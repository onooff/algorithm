def solution(arr):
    answer = [0, 0]
    size = len(arr)
    chk = [[False for j in range(size)] for i in range(size)]
    chk_cnt = size*size
    while chk_cnt > 0:
        for y in range(0, len(arr), size):
            for x in range(0, len(arr), size):
                if chk[y][x]:
                    continue
                val = arr[y][x]
                is_same = True
                for i in range(y, y+size):
                    for j in range(x, x+size):
                        if arr[i][j] != val:
                            is_same = False
                            break
                    if not is_same:
                        break
                if is_same:
                    answer[val] += 1
                    for i in range(y, y+size):
                        for j in range(x, x+size):
                            chk[i][j] = True
                    chk_cnt -= size*size
        size //= 2

    return answer
