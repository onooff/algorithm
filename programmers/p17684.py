def solution(msg):
    answer = []
    d = dict()
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(s)):
        d.setdefault(s[i], i+1)

    key = 27
    cut = 1

    while len(msg) > 0:
        if msg[:cut+1] in d and cut+1 <= len(msg):
            cut += 1
            continue
        answer.append(d[msg[:cut]])
        d.setdefault(msg[:cut+1], key)
        msg = msg[cut:]
        key += 1
        cut = 1
        if cut > len(msg):
            cut = len(msg)
        print(msg)
    print(d)
    return answer


print(solution("ABABABABABABABAB"))
