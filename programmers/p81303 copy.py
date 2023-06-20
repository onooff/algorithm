def solution(n, m, products):
    print('n=', n)
    print('m=', m)
    print('products=', products)
    cnt = dict()
    for p in products:
        name, grade = p.split()
        cnt.setdefault(name, dict())
        cnt[name].setdefault(grade, 0)
        cnt[name][grade] += 1
    print(cnt)
    p_dict = dict()
    answer = [[] for i in range(m)]
    for p in cnt:
        p_dict[p] = ''.join(
            sorted(list(cnt[p].keys()), key=lambda x: -cnt[p][x]))
        answer[ord(p_dict[p][0])-ord('A')].append(p)
    print(p_dict)
    for i in range(m):
        if len(answer[i]) == 0:
            answer[i] = '-'
            continue
        answer[i].sort(key=lambda x: (p_dict[x], x))
        answer[i] = ' '.join(answer[i])
    return answer


print(solution(3, 5, ["apple A", "apple A", "banana A", "apple B"]))
