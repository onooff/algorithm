import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    pop = heapq.heappop(scoville)
    while len(scoville) > 0 and pop <= K:
        heapq.heappush(scoville, pop+heapq.heappop(scoville)*2)
        answer += 1
        pop = heapq.heappop(scoville)
        # print(pop)

    if len(scoville) > 0 or pop >= K:
        return answer
    else:
        return -1


# print(solution([1, 2, 3, 9, 10, 12], 7))
