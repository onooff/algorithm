'''
 0
1 2
 3
4 5
 6
'''
# seven_segment_num = (
#     # 0    1      2      3      4     5     6
#     (True, True, True, False, True, True, True),  # 0
#     (False, False, True, False, False, True, False),  # 1
#     (True, False, True, True, True, False, True),  # 2
#     (True, False, True, True, False, True, True),  # 3
#     (False, True, True, True, False, True, False),  # 4
#     (True, True, False, True, False, True, True),  # 5
#     (True, True, False, True, True, True, True),  # 6
#     (True, False, True, False, False, True, False),  # 7
#     (True, True, True, True, True, True, True),  # 8
#     (True, True, True, True, False, True, True),  # 9
# )


# def print_num(segment_info):
#     # □■
#     if segment_info[0]:
#         print("□■■□")
#     else:
#         print("□□□□")

#     if segment_info[1]:
#         print("■□", end='')
#     else:
#         print("□□", end='')
#     if segment_info[2]:
#         print("□■")
#     else:
#         print("□□")

#     if segment_info[1]:
#         print("■□", end='')
#     else:
#         print("□□", end='')
#     if segment_info[2]:
#         print("□■")
#     else:
#         print("□□")

#     if segment_info[3]:
#         print("□■■□")
#     else:
#         print("□□□□")

#     if segment_info[4]:
#         print("■□", end='')
#     else:
#         print("□□", end='')
#     if segment_info[5]:
#         print("□■")
#     else:
#         print("□□")

#     if segment_info[4]:
#         print("■□", end='')
#     else:
#         print("□□", end='')
#     if segment_info[5]:
#         print("□■")
#     else:
#         print("□□")

#     if segment_info[6]:
#         print("□■■□")
#     else:
#         print("□□□□")


# for s in seven_segment_num:
#     print_num(s)
#     print("---------")


# gragh = [[0 for j in range(10)] for i in range(10)]
# for i in range(10):
#     for j in range(i+1, 10):
#         for k in range(7):
#             if seven_segment_num[i][k] != seven_segment_num[j][k]:
#                 gragh[i][j] += 1
#                 gragh[j][i] += 1


# nkpx 최대n층 k자리수 p개반전 현재x층
gragh = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2], [4, 0, 5, 3, 2, 5, 6, 1, 5, 4], [3, 5, 0, 2, 5, 4, 3, 4, 2, 3], [3, 3, 2, 0, 3, 2, 3, 2, 2, 1], [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], [
    3, 5, 4, 2, 3, 0, 1, 4, 2, 1], [2, 6, 3, 3, 4, 1, 0, 5, 1, 2], [3, 1, 4, 2, 3, 4, 5, 0, 4, 3], [1, 5, 2, 2, 3, 2, 1, 4, 0, 1], [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]
n, k, p, x = map(int, input().split())
list_x = list(map(int, list(str(x).zfill(k))))
list_n = list(map(int, list(str(n).zfill(k))))
ans = -1
test = 0
for i in range(k):
    test += gragh[list_x[i]][0]
if test <= p:
    ans -= 1


def dfs(idx, used, flag):
    global ans, gragh, k, list_n, list_x, p
    if idx == k:
        ans += 1
        return
    if flag:
        flag = False
        for i in range(list_n[idx]+1):
            if i == list_n[idx]:
                flag = True
            if used+gragh[list_x[idx]][i] <= p:
                dfs(idx+1, used+gragh[list_x[idx]][i], flag)
    else:
        for i in range(10):
            if used+gragh[list_x[idx]][i] <= p:
                dfs(idx+1, used+gragh[list_x[idx]][i], flag)


dfs(0, 0, True)
print(ans)
