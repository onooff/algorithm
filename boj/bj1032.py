'''
3
config.sys
config.inf
configures
'''

n = int(input())
ans = list(input())
for i in range(n-1):
    tmp = list(input())
    for j in range(len(ans)):
        if ans[j] != '?' and ans[j] != tmp[j]:
            ans[j] = '?'
print(''.join(ans))
