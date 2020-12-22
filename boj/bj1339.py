# import itertools
# # import time
# # st = time.time()
# n = int(input())

# sl = list()
# alpha = set()
# for i in range(n):
#     sl.append(input())
#     for j in range(len(sl[i])):
#         # print(sl[i][j])
#         alpha.add(sl[i][j])
# # sl.sort()
# # sl.sort(key=lambda x: -len(x))
# # print(alpha)

# alpha_p = list(itertools.permutations(alpha, len(alpha)))
# # print(list(alpha_p))
# print(alpha)
# ans = 0
# for p in alpha_p:
#     sum_val = 0
#     val = 9
#     alpha_dict = dict()
#     for c in p:
#         alpha_dict.setdefault(c, val)
#         val -= 1
#     for s in sl:
#         e = 1
#         for i in range(len(s)-1, -1, -1):
#             sum_val += alpha_dict[s[i]]*e
#             e *= 10
#     ans = max(ans, sum_val)
#     # print(ans)

# print(ans)
# # print(time.time()-st)


# import itertools

n = int(input())

sl = list()
alpha_dict = dict()
for i in range(n):
    sl.append(input())
    for j in range(len(sl[i])):
        c = sl[i][j]
        if sl[i][j] not in alpha_dict.keys():
            alpha_dict.setdefault(c, 0)
        alpha_dict[c] += 10**(len(sl[i])-j-1)

# print(alpha_dict)
ans = 0
# ans_set = set()
for i in range(9, 9-len(alpha_dict.keys()), -1):
    max_val = -1
    c = ''
    for j in alpha_dict.keys():
        # if j not in ans_set:
        if max_val < alpha_dict[j]*i:
            max_val = alpha_dict[j]*i
            c = j
    ans += max_val
    alpha_dict.pop(c)
    # print(c, i)
print(ans)
