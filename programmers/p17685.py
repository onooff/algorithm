def solution(words):
    answer = 0
    d = dict()
    for w in words:
        cur = d
        for i in range(len(w)):
            cur.setdefault(w[i], [dict(), 0])
            cur[w[i]][1] += 1
            cur = cur[w[i]][0]
    for w in words:
        cur = d
        for i in range(len(w)):
            if cur[w[i]][1] == 1:
                break
            cur = cur[w[i]][0]
        answer += i+1
    return answer


print(solution(["go", "gone", "guild"]))
