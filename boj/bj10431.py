t = int(input())
for tc in range(t):
    nums = list(map(int, input().split()))[1:]
    ans = [0 for i in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i, -1, -1):
            if nums[i] < nums[j]:
                ans[j] += 1

    print(tc + 1, sum(ans))
