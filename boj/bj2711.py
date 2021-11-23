n = int(input())
for _ in range(n):
    idx, s = input().split()
    idx = int(idx)-1
    print(s[:idx]+s[idx+1:])
