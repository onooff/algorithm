import sys
inputs = sys.stdin.readlines()
ans = [0, 0, 0, 0, 0]
for i in range(1, len(inputs)):
    x, y = map(int, inputs[i].rstrip().split())
    if x == 0 or y == 0:
        ans[4] += 1
    elif x > 0 and y > 0:
        ans[0] += 1
    elif x < 0 and y > 0:
        ans[1] += 1
    elif x < 0 and y < 0:
        ans[2] += 1
    elif x > 0 and y < 0:
        ans[3] += 1

for i in range(5):
    if i < 4:
        print(f"Q{i+1}: {ans[i]}")
    else:
        print(f"AXIS: {ans[i]}")
