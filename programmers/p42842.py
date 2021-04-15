def solution(brown, yellow):
    area = brown+yellow
    w = brown//2
    h = 0
    while True:
        h += 1
        w -= 1
        if h*w == area:
            break
    return [w, h]
