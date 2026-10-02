# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/max-number-of-k-sum-pairs?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def maxOperations(self, nums, k):
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        ans = 0
        for n in d:
            a = k - n
            if a not in d or d[a] <= 0:
                continue
            while d[n] > 0 and d[a] > 0:
                if n == a and d[n] < 2:
                    break
                d[n] -= 1
                d[a] -= 1
                ans += 1
        return ans


# class Solution(object):
#     def maxOperations(self, nums, k):
#         freq = {}
#         for x in nums:
#             freq[x] = freq.get(x, 0) + 1
#         ans = 0
#         for x in list(freq):
#             y = k - x
#             if y == x:
#                 ans += freq[x] // 2
#             elif y in freq:
#                 ans += min(freq[x], freq[y])
#                 freq[x] = 0
#                 freq[y] = 0
#         return ans


# 투 포인터 풀이 : 정렬해야 함
# class Solution(object):
#     def maxOperations(self, nums, k):
#         nums.sort()
#         left, right = 0, len(nums) - 1
#         ans = 0
#         while left < right:
#             s = nums[left] + nums[right]
#             if s == k:
#                 ans += 1
#                 left += 1
#                 right -= 1
#             elif s < k:
#                 left += 1
#             else:
#                 right -= 1
#         return ans
