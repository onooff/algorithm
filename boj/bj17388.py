names = ["Soongsil", "Korea", "Hanyang"]
nums = list(map(int, input().split()))
if sum(nums) >= 100:
    print("OK")
else:
    print(names[nums.index(min(nums))])
