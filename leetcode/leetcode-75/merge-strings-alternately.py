# https://leetcode.com/problems/merge-strings-alternately?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = 0
        len1 = len(word1)
        len2 = len(word2)
        l = []
        while i < len1 and i < len2:
            l.append(word1[i])
            l.append(word2[i])
            i += 1
        if len1 > len2:
            return "".join(l) + word1[i:]
        else:
            return "".join(l) + word2[i:]
