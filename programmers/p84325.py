def solution(table, languages, preference):
    d = dict()
    for t in table:
        t = t.split()
        d.setdefault(t[0], dict())
        for i in range(1, 6):
            d[t[0]].setdefault(t[i], 6-i)
    keys = list(d.keys())
    keys.sort()
    answer = ''
    most = 0
    for key in keys:
        s = 0
        for i in range(len(languages)):
            if languages[i] in d[key]:
                s += d[key][languages[i]]*preference[i]
        if s > most:
            answer = key
            most = s
    return answer


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))
