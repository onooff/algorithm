def solution(key, lock):
    blank = []
    for i in range(0, len(lock)):
        for j in range(0, len(lock)):
            if lock[i][j] == '0':
                blank.append = (i, j)

    for k in range(0, 4):
        key_tmp = [""]*len(key)
        for i in range(0, len(key)):
            for j in range(0, len(key)):
                key_tmp[j] = key[j][i]
        key = key_tmp

        for i in range(0, len(key)):
            for j in range(0, len(key)):

    return False
