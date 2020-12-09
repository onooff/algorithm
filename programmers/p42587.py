def solution(priorities, location):
    answer = 0
    while len(priorities) > 0:
        tmp = priorities.pop(0)
        if len(priorities) == 0 or tmp >= max(priorities):
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(tmp)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    return answer
