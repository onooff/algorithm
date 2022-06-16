n = int(input())
lastlast = 2
last = 7
summ = 9
for _ in range(n-1):
    lastlast, last = last, (summ*2+lastlast+2) % 1000000007
    summ += last
print(lastlast)
