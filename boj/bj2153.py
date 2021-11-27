alpha_to_num = dict()
num = 1
for az in [range(ord('a'), ord('z')+1), range(ord('A'), ord('Z')+1)]:
    for i in az:
        alpha_to_num.setdefault(chr(i), num)
        num += 1

lim = alpha_to_num['Z']*20+1
primes = {i for i in range(1, lim)}
for i in range(2, lim):
    if i in primes:
        tmp = i+i
        while tmp < lim:
            primes.discard(tmp)
            tmp += i

s = input()
s = list(map(lambda x: alpha_to_num[x], list(s)))
if sum(s) in primes:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
