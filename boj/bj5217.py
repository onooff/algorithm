import sys
inputs = sys.stdin.readlines()
memo = dict()
for i in range(1, len(inputs)):
    num = int(inputs[i])
    sys.stdout.write(f"Pairs for {num}:")
    if num not in memo:
        a, b = 1, num-1
        ans = ''
        while a < b:
            ans += f" {a} {b},"
            a, b = a+1, b-1
        if len(ans) > 0:
            ans = ans[:-1]
        ans += '\n'
        memo.setdefault(num, ans)
    sys.stdout.write(memo[num])
