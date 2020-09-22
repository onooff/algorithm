answer = ["ICN"]


def dfs(tickets, start):
    global answer
    for i in range(0, len(tickets)):
        if tickets[i][0] == start:
            t = tickets.pop(i)
            answer.append(t[1])
            dfs(tickets, t[1])
            if len(tickets) == 0:
                return
            answer.pop(len(answer)-1)
            tickets.insert(i, t)


def solution(tickets):
    tickets.sort()
    print(tickets)
    dfs(tickets, "ICN")
    return answer


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print("--------------")
# print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
      "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
