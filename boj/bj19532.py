a, b, c, d, e, f = map(int, input().split())
# 브루트포스
# ans = False
# for x in range(-999, 1000):
#     for y in range(-999, 1000):
#         if a*x+b*y == c and d*x+e*y == f:
#             print(x, y)
#             ans = True
#             break
#     if ans:
#         break

# 수학
print((c*e-b*f)//(a*e-b*d), (c*d-a*f)//(b*d-a*e))
