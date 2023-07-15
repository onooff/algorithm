while True:
    s = input()
    if s == "end":
        break

    mo = ("a", "e", "i", "o", "u")
    mo_cnt = 0
    za_cnt = 0
    last = None
    is_ans = False
    for c in s:
        if c in mo:
            is_ans = True
            za_cnt = 0
            mo_cnt += 1
            if mo_cnt >= 3:
                is_ans = False
                break
        else:
            mo_cnt = 0
            za_cnt += 1
            if za_cnt >= 3:
                is_ans = False
                break

        if last == c:
            if not (c == "o" or c == "e"):
                is_ans = False
                break

        last = c
    if is_ans:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
