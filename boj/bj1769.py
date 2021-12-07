s = input()
cnt = 0
while len(s) > 1:
    tmp = 0
    for n in s:
        tmp += int(n)
    s = str(tmp)
    cnt += 1
print(cnt)
if int(s) % 3 == 0:
    print("YES")
else:
    print("NO")
