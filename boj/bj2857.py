import sys
inputs = sys.stdin.readlines()
ans = str()
for i in range(len(inputs)):
    if "FBI" in inputs[i]:
        ans += str(i+1)+' '
if ans == '':
    ans = "HE GOT AWAY!"
print(ans)
