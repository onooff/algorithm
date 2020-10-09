def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    index = 0
    for st in skill_trees:
        isOK = True
        for s in st:
            if s in skill:
                if s != skill[index]:
                    isOK = False
                    break
                else:
                    index += 1
        if isOK:
            answer += 1
        index = 0

    return answer
