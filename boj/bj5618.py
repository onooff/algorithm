def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


n = int(input())
nums = list(map(int, input().split()))
nums.sort()
g = nums[0]
for i in range(1, n):
    g = gcd(g, nums[i])

ans = set()
for i in range(1, int(g ** 0.5) + 1):
    if g % i == 0:
        ans.add(i)
        ans.add(g // i)
for a in sorted(ans):
    print(a)
