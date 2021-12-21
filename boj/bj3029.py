t1 = list(map(int, input().split(":")))
t2 = list(map(int, input().split(":")))

t1 = t1[0] * 3600 + t1[1] * 60 + t1[2]
t2 = t2[0] * 3600 + t2[1] * 60 + t2[2] + 86400

ans = t2 - t1
if ans > 86400:
    ans -= 86400
ans_h = ans // 3600
ans %= 3600
ans_m = ans // 60
ans %= 60
ans_s = ans
print(f"{ans_h:0>2}:{ans_m:0>2}:{ans_s:0>2}")
