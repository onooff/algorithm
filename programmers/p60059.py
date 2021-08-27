def turn(key_list, key_size):
    for k in key_list:
        k[0], k[1] = k[1], key_size-1-k[0]


def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)

    key_list = list()
    for i in range(key_size):
        for j in range(key_size):
            if key[i][j] == 1:
                key_list.append([i, j])

    lock_list = list()
    for i in range(lock_size):
        for j in range(lock_size):
            if lock[i][j] == 0:
                lock_list.append((i, j))

    if len(key_list) == 0 or len(key_list) < len(lock_list):
        return False
    if len(lock_list) == 0:
        return True
    first_lock = lock_list[0]
    last_lock = lock_list[len(lock_list)-1]
    lock_set = set(lock_list)
    answer = False
    for t in range(4):
        for i in range(-key_size+1+first_lock[0], last_lock[0]+1):
            for j in range(-key_size+1+first_lock[1], last_lock[1]+1):
                cnt = 0
                for k in key_list:
                    chk = (k[0]+i, k[1]+j)
                    if chk in lock_set:
                        cnt += 1
                        if cnt == len(lock_set):
                            answer = True
                            break
                    elif 0 <= chk[0] < lock_size and 0 <= chk[1] < lock_size:
                        break
                if answer:
                    break
            if answer:
                break
        if answer:
            break

        if t < 3:
            turn(key_list, key_size)
    return answer


print(solution(	[[1, 0], [0, 0]],
                [[0, 1, 1], [1, 1, 1], [1, 1, 0]]))
