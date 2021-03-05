'''
최대값 찾고
최대값 오른쪽으로 다 들어내고
이후 왼쪽부터 감소할때 끊어주기
'''
import copy
t = int(input())

for tc in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    sorted_p = copy.deepcopy(p)
    sorted_p.sort()
    sorted_p.reverse()
    set_p = set(p)
    max_val = 0
    last_max_idx = n
    cnt = 0
    while cnt < n:
        # print('why', max_val, sorted_p[max_val], set_p, sorted_p[0] in set_p)
        max_idx = p.index(sorted_p[max_val])
        for i in range(max_idx, last_max_idx):
            print(p[i], end=' ')
            set_p.discard(p[i])
            cnt += 1
        last_max_idx = max_idx
        for i in range(max_val, n):
            if sorted_p[i] in set_p:
                # print(i)
                max_val = i
                break
    print()
