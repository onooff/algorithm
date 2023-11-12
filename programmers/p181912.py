def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        n = int(str[s : s + l])
        if n > k:
            answer.append(n)
    return answer
