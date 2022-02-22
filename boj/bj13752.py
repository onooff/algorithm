h = ''
ans = list()
for _ in range(81):
    ans.append(h)
    h += '='
n = int(input())
for _ in range(n):
    print(ans[int(input())])
