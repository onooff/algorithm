# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxx = max(candies)
        ans = []
        for candy in candies:
            if candy + extraCandies >= maxx:
                ans.append(True)
            else:
                ans.append(False)
        return ans
