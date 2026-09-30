# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
