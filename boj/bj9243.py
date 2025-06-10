n = int(input())
s1, s2 = input(), input()

diff = True if n % 2 == 0 else False
ans = "Deletion succeeded"

for i in range(len(s1)):
    if (s1[i] == s2[i]) != diff:
        ans = "Deletion failed"
        break

print(ans)
