'''
3
26 40 83
49 60 57
13 89 99
'''

n = int(input())
info = list()
for i in range(n):
    info.append(list(map(int, input().split())))

ans = [info[0]]

for i in range(1, n):
    ans.append([
        min(ans[i-1][1]+info[i][0], ans[i-1][2]+info[i][0]),
        min(ans[i-1][0]+info[i][1], ans[i-1][2]+info[i][1]),
        min(ans[i-1][0]+info[i][2], ans[i-1][1]+info[i][2])
    ])

print(min(ans[n-1]))
