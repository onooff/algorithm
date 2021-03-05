def u(a, b):
    while True:
        if b % a == 0:
            return a
        else:
            a, b = b % a, a


n, m = map(int, input().split())
a = list(map(int, input().split()))
# a.sort()
b = list(map(int, input().split()))

# for bj in b:
#     gcd = a[0]+bj
#     for i in range(1, n):
#         tmp = a[i]+bj
#         while True:
#             if tmp % gcd == 0:
#                 break
#             else:
#                 gcd, tmp = tmp % gcd, gcd
#     print(gcd, end=' ')

for bj in b:
    cnt = 0
    gcds = set()
    while len(gcds) != 1:
        if cnt == 0:
            for i in range(0, len(a), 2):
                if i == n-1:
                    gcds.add(a[i]+bj)
                else:
                    gcds.add(
                        u(
                            min(a[i]+bj, a[i+1]+bj), max(a[i]+bj, a[i+1]+bj)
                        )
                    )
        else:
            gcds = list(gcds)
            # gcds.sort()
            tmp = set()
            for i in range(0, len(gcds), 2):
                if i == len(gcds)-1:
                    tmp.add(gcds[i])
                else:
                    # print(gcds[i], gcds[i+1])
                    tmp.add(
                        u(min(gcds[i], gcds[i+1]), max(gcds[i], gcds[i+1]))
                    )
            gcds = tmp
        cnt += 1
        # print(gcds)
    print(list(gcds)[0], end=' ')
