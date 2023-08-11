n = int(input())
ans = list()

num = 0
while len(ans) < n:
    num += 1
    if num > 3:
        num = ans.pop()
        continue
    ans.append(num)
    is_ok = True
    for chk_len in range(1, (len(ans) // 2) + 1):
        is_bad = True
        for i in range(chk_len):
            if ans[len(ans) - chk_len + i] != ans[len(ans) - chk_len - chk_len + i]:
                is_bad = False
                break
        if is_bad:
            is_ok = False
            break
    if is_ok:
        num = 0
    else:
        num = ans.pop()
print(*ans, sep="")
