# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def isSubsequence(self, s, t):
        si = 0
        ti = 0
        while si < len(s) and ti < len(t):
            while ti < len(t) and t[ti] != s[si]:
                ti += 1
            if si < len(s) and ti < len(t) and t[ti] == s[si]:
                si += 1
                ti += 1
        if si >= len(s):
            return True
        return False


# class Solution(object):
#     def isSubsequence(self, s, t):
#         i = j = 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return i == len(s)
