# import math
# t = int(input())

# for tc in range(t):
#     n = int(input())
#     if n % 2 == 1:
#         print('yes')
#     else:
#         nn = int(math.sqrt(n))
#         ans_is_yes = False
#         for i in range(3, nn, 2):
#             if n % i == 0:
#                 ans_is_yes = True
#                 break
#         if ans_is_yes:
#             print('yes')
#         else:
#             print('no')


# import math
# t = int(input())

# for tc in range(t):
#     n = int(input())
#     if n % 2 == 1:
#         print('yes')
#     else:
#         nn = int(math.sqrt(math.sqrt(n)))
#         is_prime = [1 for i in range(nn+1)]
#         is_prime[0] = 0
#         is_prime[1] = 0
#         prime = set()
#         for i in range(nn+1):
#             if is_prime[i] == 1:
#                 prime.add(i)
#                 for j in range(2*i, nn+1, i):
#                     is_prime[j] = 0
#         prime.discard(2)

#         ans_is_yes = False
#         for p in prime:
#             if n % p == 0:
#                 ans_is_yes = True
#                 break
#         if ans_is_yes:
#             print('yes')
#         else:
#             print('no')


t = int(input())

for tc in range(t):
    n = int(input())
    while n % 2 == 0:
        n //= 2
    if n == 1:
        print('no')
    else:
        print('yes')
