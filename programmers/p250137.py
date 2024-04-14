def solution(bandage, health, attacks):
    cur = health
    last = 0
    for a in attacks:
        t, d = a
        term = t - last - 1
        cur = min(health, cur + (term * bandage[1] + bandage[2] * (term // bandage[0])))
        cur -= d
        if cur <= 0:
            cur = -1
            break
        last = t
    return cur
