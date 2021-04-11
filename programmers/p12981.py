def solution(n, words):
    answer = [0, 0]

    player = -1
    turn = -1
    last = words[0][0]
    word_set = set()
    for w in words:
        # print(last[-1], w[0])
        player = (player+1) % n
        if player == 0:
            turn += 1
        if last[-1] != w[0]:
            answer = [player+1, turn+1]
            break
        else:
            if w in word_set:
                answer = [player+1, turn+1]
                break
            last = w
            word_set.add(w)
    return answer


print(solution(3,	["tank", "kick", "know", "wheel",
                   "land", "dream", "mother", "robot", "tank"]))
