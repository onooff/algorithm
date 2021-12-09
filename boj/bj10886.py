cnt = 0
n = int(input())
for _ in range(n):
    cnt += int(input())
if n-cnt > cnt:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
