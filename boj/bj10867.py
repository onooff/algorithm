input()
nums = set(map(int, input().split()))
nums = list(nums)
nums.sort()
for n in nums:
    print(n, end=' ')
