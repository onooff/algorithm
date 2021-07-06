def solution(stones, k):
    dq = list()
    answer = 222222222
    for i in range(len(stones)):
        while(len(dq) > 0 and dq[0][1] < i-k+1):
            dq.pop(0)
        while(len(dq) > 0 and dq[len(dq)-1][0] < stones[i]):
            dq.pop()
        dq.append((stones[i], i))
        if(i > -k-1 and dq[0][0] < answer):
            answer = dq[0][0]
    return answer

# def solution(stones, k):
#     m = max(stones[0:k])
#     ans = m
#     for i in range(1, len(stones)-k+1):
#         if stones[i-1] == m:
#             tmp=stones[i:i+k]
#             tmp.sort()
#             m = tmp[k-1]
#             ans = min(ans, m)
#     return ans

# def solution(stones, k):
#     summ = sum(stones[0:k])
#     min_sum=summ
#     ans = stones[0:k]
#     for i in range(1, len(stones)-k+1):
#         summ-=stones[i-1]
#         summ+=stones[i+k-1]
#         # print(stones[i:i+k], summ)
#         if min_sum>summ:
#             min_sum=summ
#             ans = stones[i:i+k]
#     return max(ans)
