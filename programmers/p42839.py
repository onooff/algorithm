import math
import itertools


def solution(numbers):
    answer = set()
    length = len(numbers)
    num_list = list(numbers)

    for i in range(1, length+1):
        perm_num_list = list(itertools.permutations(num_list, i))
        for n in perm_num_list:
            chk = int(''.join(n))
            # print(chk)
            if chk <= 1:
                continue
            is_ans = True
            for d in range(2, int(math.sqrt(chk))+1):
                if chk % d == 0:
                    is_ans = False
                    break
            if is_ans:
                answer.add(chk)
                # print(chk)

    return len(answer)
