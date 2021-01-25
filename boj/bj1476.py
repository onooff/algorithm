# e, s, m = map(int, input().split())
# ee, ss, mm = 0, 0, 0

# ans = 1
# while True:
#     if e == ee+1 and s == ss+1 and m == mm+1:
#         print(ans)
#         break
#     else:
#         ee = (ee+1) % 15
#         ss = (ss+1) % 28
#         mm = (mm+1) % 18
#         ans += 1


e, s, m = map(int, input().split())

ans = s-1
while True:
    if (ans % 15)+1 == e and (ans % 19)+1 == m:
        print(ans+1)
        break
    else:
        ans += 28
