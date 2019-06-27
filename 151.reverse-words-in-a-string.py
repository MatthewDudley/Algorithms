#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
# Author: Matthew Dudley
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(c for c in s.split()[::-1])

