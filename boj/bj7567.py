bowls = input()

ans = 10
for i in range(1, len(bowls)):
    if bowls[i] == bowls[i-1]:
        ans += 5
    else:
        ans += 10
print(ans)
