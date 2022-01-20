import math
m = int(input())
n = int(input())
minn = math.ceil(math.sqrt(m))
summ = 0
for i in range(minn, math.floor(math.sqrt(n))+1):
    summ += i*i
if summ == 0:
    print(-1)
else:
    print(f"{summ}\n{minn*minn}")
