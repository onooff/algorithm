n = int(input())
l = input().split()

for ans in [[_ for _ in range(9, 9 - n - 1, -1)], [_ for _ in range(n + 1)]]:
    is_ans = False
    while not is_ans:
        is_ans = True
        for i in range(n):
            if l[i] == ">":
                if ans[i] < ans[i + 1]:
                    ans[i], ans[i + 1] = ans[i + 1], ans[i]
                    is_ans = False
            else:  # <
                if ans[i] > ans[i + 1]:
                    ans[i], ans[i + 1] = ans[i + 1], ans[i]
                    is_ans = False
    print(*ans, sep="")
