d = [
    [0, 1],
    [1, -1],
    [0, 1],
    [0, 0],
]
n, r, c = map(int, input().split())

ans = 0
s = (0, 0)
n = (2**n)//2
while True:
    for z in range(4):
        if (r in range(s[0]+n)) and (c in range(s[1]+n)):
            n //= 2
            break
        else:
            ans += n*n
            if z == 3:
                break
            s = (s[0]+d[z][0]*n, s[1]+d[z][1]*n)
            # print(n,s)
    if n == 0:
        break
print(ans)


# print(ans,end=' ')


# d = [
#     [0, 1],
#     [1, -1],
#     [0, 1],
#     [0, 0],
# ]
# nn = int(input())

# for r in range(2**nn):
#     for c in range(2**nn):
#         # n, r, c = map(int, input().split())

#         ans = 0
#         s = (0, 0)
#         n = (2**nn)//2
#         while True:
#             for z in range(4):
#                 if (r in range(s[0]+n)) and (c in range(s[1]+n)):
#                     n //= 2
#                     break
#                 else:
#                     ans += n*n
#                     if z == 3:
#                         break
#                     s = (s[0]+d[z][0]*n, s[1]+d[z][1]*n)
#                     # print(n,s)
#             if n == 0:
#                 break
#         # print(r,c,ans)
#         print(ans,end=' ')
#     print()
