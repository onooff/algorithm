import sys

input = sys.stdin.readline

chk = int(input())
n = int(input())
summ = 0
for _ in range(n):
    a, b = map(int, input().split())
    summ += a * b

if chk == summ:
    print("Yes")
else:
    print("No")
