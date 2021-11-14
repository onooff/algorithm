import math

n, m = map(int, input().split(':'))
gcd = math.gcd(n, m)
print(str(n//gcd)+":"+str(m//gcd))
