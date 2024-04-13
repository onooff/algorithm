def solution(babbling):
    answer = 0
    for b in babbling:
        bb = b
        is_ok = True
        last = "*"
        while len(b) > 0:
            if len(b) < 2:
                is_ok = False
                break
            else:
                sub = b[:2]
                if sub == "ye" or sub == "ma":
                    if sub == last:
                        is_ok = False
                        break
                    last = sub
                    b = b[2:]
                    continue
                sub = b[:3]
                if sub == "aya" or sub == "woo":
                    if sub == last:
                        is_ok = False
                        break
                    last = sub
                    b = b[3:]
                    continue
                is_ok = False
                break
        if is_ok:
            answer += 1
    return answer
