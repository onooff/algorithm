answer = 99999999999999


def my_str_comp(str1, str2):
    diff_index = -1
    for i in range(0, len(str1)):
        if (str1[i] != str2[i]):
            if (diff_index != -1):
                return -1
            else:
                diff_index = i
    return diff_index


def dfs(begin, target, words, depth):
    global answer
    for i in range(0, len(words)):
        if my_str_comp(begin, words[i]) >= 0:
            if target == words[i]:
                answer = min(answer, depth)
                return
            else:
                temp = words.pop(i)
                dfs(temp, target, words, depth+1)
                words.insert(i, temp)


def solution(begin, target, words):
    dfs(begin, target, words, 1)
    if answer == 99999999999999:
        return 0
    return answer


print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
