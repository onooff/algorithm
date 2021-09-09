def solution(weights, head2head):
    size = len(weights)
    boxers = list()
    for i in range(size):
        game = 0
        win = 0
        heavy_win = 0
        for j in range(size):
            if head2head[i][j] == 'W' or head2head[i][j] == 'L':
                game += 1
                if head2head[i][j] == 'W':
                    win += 1
                    if weights[i] < weights[j]:
                        heavy_win += 1
        winlate = 0
        if game > 0:
            winlate = win/game
        boxers.append((i+1, weights[i], heavy_win, winlate))
    boxers.sort(key=lambda x: x[0])
    boxers.sort(key=lambda x: -x[1])
    boxers.sort(key=lambda x: -x[2])
    boxers.sort(key=lambda x: -x[3])
    answer = list()
    for b in boxers:
        answer.append(b[0])
    return answer
