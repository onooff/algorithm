import sys
inputs = sys.stdin.readlines()
n = int(inputs[1])
ans = 'S'
for i in range(2, len(inputs)):
    if int(inputs[i]) > n:
        ans = 'N'
        break
print(ans)
