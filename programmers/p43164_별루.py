answer = ["ICN"]
ret = []


def dfs(tickets, start):
    global answer
    global ret
    if len(tickets) == 0:
        print(answer)
        # ret = answer.copy()
    for i in range(0, len(tickets)):
        if tickets[i][0] == start:
            t = tickets.pop(i)
            answer.append(t[1])
            dfs(tickets, t[1])
            answer.pop(len(answer)-1)
            tickets.insert(i, t)


def solution(tickets):
    global ret
    ret = []
    tickets.sort()
    dfs(tickets, "ICN")
    return ret


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print("--------------")
print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
      "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
