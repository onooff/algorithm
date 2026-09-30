# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def reverseVowels(self, s):
        ans = list(s)
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and ans[l] not in vowels:
                l += 1
            while l < r and ans[r] not in vowels:
                r -= 1
            if l < r:
                ans[l], ans[r] = ans[r], ans[l]
            l += 1
            r -= 1
        return "".join(ans)
