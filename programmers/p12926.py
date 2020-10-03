def solution(s="", n=2):
    answer = ""
    for c in s:
        if c == " ":
            answer += " "
        elif 65 <= ord(c) <= 90:
            newC = ord(c)+n
            if newC >= 91:
                newC -= 26
            answer += chr(newC)
        elif 97 <= ord(c) <= 122:
            newC = ord(c)+n
            if newC >= 123:
                newC -= 26
            answer += chr(newC)

    return answer


print(solution(	"AB", 1))
