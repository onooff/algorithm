import sys
inputs = sys.stdin.readlines()
ans = [0]
d = 1
while d < 100:
    ans.append(d+ans[-1])
    d += 2
for i in range(1, len(inputs)):
    print(ans[(int(inputs[i])+1)//2])
