import math
t = int(input())

for tc in range(t):
    s1 = input()
    s2 = input()

    if not(s1[0] == s2[0] and s1[len(s1)-1] == s2[len(s2)-1]):
        print('-1')
        continue

    n1 = len(s1)
    n2 = len(s2)

    n_gcd = math.gcd(n1, n2)
    n_lcm = (n1*n2)//n_gcd

    d1 = n_lcm//n1
    d2 = n_lcm//n2

    s1 = s1*d1
    s2 = s2*d2

    if s1 == s2:
        print(s1)
    else:
        print('-1')
