def solution(s):
    answer = []
    s = s[1:len(s)-1]
    ls = list()
    tmp = list()
    num = ""
    i = 0
    while i < len(s):
        if s[i] == "{":
            tmp = list()
        elif str.isdigit(s[i]):
            num += s[i]
        elif s[i] == ",":
            tmp.append(int(num))
            num = ""
        elif s[i] == "}":
            tmp.append(int(num))
            num = ""
            tmp.sort()
            ls.append(tmp)
            i += 1
        i += 1

    ls.sort(key=lambda x: len(x))
    # print(ls)
    answer.append(ls[0][0])
    for i in range(len(ls)-1):
        for j in range(len(ls[i])):
            if ls[i][j] != ls[i+1][j]:
                answer.append(ls[i+1][j])
                break
        if len(answer) < len(ls[i])+1:
            answer.append(ls[i+1][len(ls[i+1])-1])

    return answer


print(solution(	"{{2},{2,1},{2,1,3},{2,1,3,4}}"))
