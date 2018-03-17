#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      nick <starshiping[at]gmail.com>
# File:        q3_Manacher.py
# Create Date: 2018-03-15 23:15:05
# Usage:       q3_Manacher.py
# Descripton:   


class Solution:
    # @return a string
    def longestPalindrome(self, s):
        start = end = 0
        for i in range(0, len(s)):
            len1 = self.expandAtCenter(s, i, i)
            len2 = self.expandAtCenter(s, i, i+1)
            length = max(len1, len2)
            if (length > end - start):
                start = i - (length-1)/2
                end = i + length/2
        return s[start : end+1]
        
    def expandAtCenter(self, s, left, right):
        L = left
        R = right
        while ( L>=0 and R<len(s) and (s[L] is s[R]) ):
            L -= 1
            R += 1
        return R - L - 1

# debug
s = Solution()
print s.longestPalindrome('ASBAASBAAA')

        