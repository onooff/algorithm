# 답도 안나오고 시간초과 ㅠㅠ
# def solution(people, limit):
#     boat = [0]
#     needNewBoat = True
#     for p in people:
#         for i in range(len(boat)):
#             if boat[i]+p <= limit:
#                 boat[i] += p
#                 needNewBoat = False
#                 break
#         if needNewBoat:
#             boat.append(p)
#         else:
#             needNewBoat = True
#     # print(boat)
#     return len(boat)
import math


def solution(people, limit):
    ans = 0
    people.sort()  # sort만 수행했을 때 최대 수행시간 4.90ms
    # ㅋㅋ 두명만 탈 수 있는거엿나 도랏내
    left = 0
    right = len(people)-1
    while left < right:
        if people[left]+people[right] <= limit:
            ans += 1
            left += 1
            right -= 1
        else:
            ans += 1
            right -= 1
    if left == right:
        ans += 1
    return ans


print(solution(	[70, 50, 80, 50, 50], 100))
