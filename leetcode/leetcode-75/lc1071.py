# 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        ans = ""
        len1 = len(str1)
        len2 = len(str2)
        for i in range(1, min(len1, len2) + 1):
            if (len1 % i == 0) and (len2 % i == 0):
                s = str1[:i]
                if s * (len1 // i) == str1 and s * (len2 // i) == str2:
                    ans = s
        return ans


# class Solution:
#     def gcdOfStrings(self, str1, str2):
#         if str1 + str2 != str2 + str1:
#             return ""

#         a = len(str1)
#         b = len(str2)

#         while b != 0:
#             a, b = b, a % b

#         return str1[:a]
