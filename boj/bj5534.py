import sys

inputs = sys.stdin.readlines()

target = inputs[1].rstrip()
ans = 0

for i in range(2, len(inputs)):
    cur = inputs[i].rstrip()
    is_ans = False
    for idx in range(len(cur)):
        if cur[idx] == target[0]:
            d = 1
            while idx + d * (len(target) - 1) < len(cur):
                if cur[idx : idx + d * (len(target) - 1) + 1 : d] == target:
                    is_ans = True
                    break
                d += 1
            if is_ans:
                break
    if is_ans:
        ans += 1

print(ans)
