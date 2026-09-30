# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def increasingTriplet(self, nums):
        inf = float("inf")
        ans = [inf, inf, inf]
        for num in nums:
            if num < ans[0]:
                ans[0] = num
            elif num < ans[1] and num > ans[0]:
                ans[1] = num
            elif num > ans[1]:
                return True

        ans = [float("-inf"), float("-inf"), float("-inf")]
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num > ans[0]:
                ans[0] = num
            elif num > ans[1] and num < ans[0]:
                ans[1] = num
            elif num < ans[1]:
                return True

        return False


# class Solution(object):
#     def increasingTriplet(self, nums):
#         first = second = float("inf")

#         for num in nums:
#             if num <= first:
#                 first = num
#             elif num <= second:
#                 second = num
#             else:
#                 return True

#         return False
