import sys
inputs = sys.stdin.readlines()
for i in range(1, len(inputs)):
    a, b, c = map(int, inputs[i].split())
    ans = "Yes"
    if c == 0 and b % 2 == 1:
        a -= 2
    else:
        a -= c
    if a < 0 or a % 2 == 1:
        ans = "No"
    print(ans)
