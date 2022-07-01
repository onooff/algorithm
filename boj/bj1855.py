n = int(input())
s = input()
solve = [s[i:i+n] for i in range(0, len(s), n)]
for i in range(1, len(solve), 2):
    solve[i] = solve[i][::-1]
ans = list()
for i in range(n):
    for j in range(len(solve)):
        if len(solve[j]) > i:
            ans.append(solve[j][i])
print(''.join(ans))
