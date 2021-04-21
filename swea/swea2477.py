t = int(input())

for tc in range(t):
    n, m, k, a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))

    a_dict = dict()
    b_dict = dict()
    t_dict = dict()
    for i in range(len(a_list)):
        a_dict.setdefault(i, [-1, 0])
    for i in range(len(b_list)):
        b_dict.setdefault(i, [-1, 0])
    for i in range(len(t_list)):
        t_dict.setdefault(i, [0, 0])

    a_empty_q = [i for i in range(len(a_list))]
    b_empty_q = [i for i in range(len(b_list))]
    a_wating_q = list()
    b_wating_q = list()
    t_num = 0
    time = -1
    complete_cnt = 0
    while complete_cnt < k:
        time += 1
        while len(t_list) > 0 and t_list[0] <= time:
            t_list.pop(0)
            a_wating_q.append(t_num)
            t_num += 1
        for i in range(len(a_list)):
            if a_dict[i][1] > 0:
                a_dict[i][1] -= 1
                if a_dict[i][1] == 0:
                    a_empty_q.append(i)
                    b_wating_q.append(a_dict[i][0])
                    t_dict[a_dict[i][0]][0] = i
        for i in range(len(b_list)):
            if b_dict[i][1] > 0:
                b_dict[i][1] -= 1
                if b_dict[i][1] == 0:
                    b_empty_q.append(i)
                    t_dict[b_dict[i][0]][1] = i
                    complete_cnt += 1
        a_empty_q.sort()
        b_empty_q.sort()
        while len(a_wating_q) > 0 and len(a_empty_q) > 0:
            working = a_empty_q.pop(0)
            a_dict[working][0] = a_wating_q.pop(0)
            a_dict[working][1] = a_list[working]
        while len(b_wating_q) > 0 and len(b_empty_q) > 0:
            working = b_empty_q.pop(0)
            b_dict[working][0] = b_wating_q.pop(0)
            b_dict[working][1] = b_list[working]
        # debug
        # print('------', time, '------')
        # print(a_dict, a_wating_q, a_empty_q)
        # print(b_dict, b_wating_q, b_empty_q)
        # print(t_list, complete_cnt)
    chk = (a-1, b-1)
    ans = 0
    for k in t_dict:
        # print(k, chk, t_dict[k])
        if tuple(t_dict[k]) == chk:
            ans += (k+1)
    if ans == 0:
        ans = -1
    print('#'+str(tc+1), ans)
