# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


# class Solution(object):
#     def moveZeroes(self, nums):
#         z = 0
#         for i in range(len(nums)):
#             while nums[z] != 0:
#                 z += 1
#                 if z >= len(nums):
#                     return
#             if i > z and nums[i] != 0:
#                 nums[i], nums[z] = nums[z], nums[i]
