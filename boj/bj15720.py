import sys

input = sys.stdin.readline

n = min(list(map(int, input().rstrip().split())))
b = sorted(list(map(int, input().rstrip().split())), key=lambda x: -x)
s = sorted(list(map(int, input().rstrip().split())), key=lambda x: -x)
d = sorted(list(map(int, input().rstrip().split())), key=lambda x: -x)

summ = sum(b) + sum(s) + sum(d)
dis_summ = summ
for i in range(n):
    dis_summ -= (b[i] + s[i] + d[i]) // 10

print(summ)
print(dis_summ)
