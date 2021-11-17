s = input()
ans = 1
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        ans = 0
        break
print(ans)
