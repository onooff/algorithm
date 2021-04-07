# ans = [-1, 9999999]


# def go(d, keys, now, min_val, max_val):
#     global ans
#     if now == len(keys):
#         print('무야호', ans, [min_val, max_val])
#         if ans[1]-ans[0]+1 > (max_val-min_val+1):
#             ans[0] = min_val
#             ans[1] = max_val
#         return

#     l = d[keys[now]]
#     # print(l)
#     for i in l:
#         go(d, keys, now+1, min(min_val, i), max(max_val, i))


# def solution(gems):
#     global ans
#     d = dict()
#     for i in range(len(gems)):
#         if gems[i] not in d:
#             d.setdefault(gems[i], set())
#         d[gems[i]].add(i)
#     # print(d)
#     k = list(d.keys())
#     go(d, k, 0, 999999, -1)

#     return [ans[0]+1, ans[1]+1]


# print(solution(	["DIA", "RUBY", "RUBY", "DIA",
#                  "DIA", "EMERALD", "SAPPHIRE", "DIA"]))


# def solution(gems):
#     d = dict()
#     for i in range(len(gems)):
#         if gems[i] not in d:
#             d.setdefault(gems[i], 0)
#         d[gems[i]] += 1
#     for i in range(len(gems)-1, -1, -1):
#         if d[gems[i]] > 1:
#             d[gems[i]] -= 1
#         else:
#             break
#     for j in range(len(gems)):
#         if d[gems[i]] > 1:
#             d[gems[i]] -= 1
#         else:
#             break
#     return [j+1, i+1]

# def solution(gems):
#     d = dict()
#     for i in range(len(gems)):
#         if gems[i] not in d:
#             d.setdefault(gems[i], 0)
#         # d[gems[i]] += 1
#     kl = list(d.keys())
#     # print(kl)
#     for i in range(len(kl)-1, len(gems)):
#         for j in range(0, len(gems)):
#             if j+i+1 > len(gems):
#                 break
#             tmp = set(gems[j:j+i+1])
#             # print(j, j+i+1, tmp)
#             if len(tmp) == len(kl):
#                 return [j+1, j+i+1]
# return answer


# print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# print(solution(		["DIA", "RUBY", "RUBY", "DIA",
#                   "DIA", "EMERALD", "SAPPHIRE", "DIA"]))

def solution(gems):
    answer = []
    gem_set = set(gems)
    d = dict()
    cnt = 0
    l = 9999999
    ans = list()
    tmp = set()
    min_val = 0
    for i in range(len(gems)):
        if gems[i] not in d:
            cnt += 1
            d.setdefault(gems[i], i)
            tmp.add(i)
        else:
            tmp.discard(d[gems[i]])
            if d[gems[i]] == min_val:
                if len(tmp) == 0:
                    min_val = i
                else:
                    min_val = min(tmp)
            d[gems[i]] = i
            tmp.add(i)
        if cnt == len(gem_set):
            if i-min_val < l:
                l = i-min_val
                ans = [min_val+1, i+1]
            if l == len(gem_set)-1:
                break
    return ans


print(solution(['DIA', 'EM', 'EM', 'RUB', 'DIA']))
