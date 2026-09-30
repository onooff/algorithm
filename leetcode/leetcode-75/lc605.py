# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        length = len(flowerbed)
        for i in range(length):
            if (
                (i == 0 or flowerbed[i - 1] == 0)
                and (i == length - 1 or flowerbed[i + 1] == 0)
                and flowerbed[i] == 0
            ):
                n -= 1
                flowerbed[i] = 1
            if n == 0:
                return True
        return False
