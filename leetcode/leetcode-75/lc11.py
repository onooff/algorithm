# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def maxArea(self, h):
        l, r = 0, len(h) - 1
        ans = 0
        while l < r:
            tmp = (r - l) * min(h[l], h[r])
            ans = max(ans, tmp)
            if h[l] <= h[r]:
                l += 1
            else:
                r -= 1
        return ans
