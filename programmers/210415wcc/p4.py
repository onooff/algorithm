# import copy


# def solution(n, z, roads, queries):
#     answer = []
#     d = dict()
#     default = dict()
#     for i in range(n):
#         d.setdefault(i, [0 for j in range(n)])
#         default.setdefault(i, 0)
#     for r in roads:
#         d[r[0]][r[1]] = r[3]
#     dp = dict()
#     bfs = list()
#     for i in range(n):
#         bfs.append(i, 0)
#     while True:
#         tmp = copy.deepcopy(default)
#         for b in bfs:
#             for i in range(len(d[b[0]])):
#                 get = d[b[0]][i]
#                 if i == b[0]:
#                     get = z
#                 tmp[i] = max(tmp[i], get[z])

#     return answer


# '''
# 가만히+z
# 이동+edge
# 몰라
# '''
