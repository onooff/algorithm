# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def productExceptSelf(self, nums):
        ll = [nums[0]] * len(nums)
        rl = [nums[-1]] * len(nums)
        for i in range(1, len(nums)):
            ll[i] = nums[i] * ll[i - 1]
            rl[-(1 + i)] = nums[-(1 + i)] * rl[-(1 + i - 1)]
        ans = [1] * len(nums)
        for i in range(len(nums)):
            l = 1 if i == 0 else ll[i - 1]
            r = 1 if i == len(nums) - 1 else rl[i + 1]
            ans[i] = l * r
        return ans


# def productExceptSelf(self, nums):
#     ans = [1] * len(nums)

#     prefix = 1
#     for i in range(len(nums)):
#         ans[i] = prefix
#         prefix *= nums[i]

#     suffix = 1
#     for i in range(len(nums) - 1, -1, -1):
#         ans[i] *= suffix
#         suffix *= nums[i]

#     return ans
