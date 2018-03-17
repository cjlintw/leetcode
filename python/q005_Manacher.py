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
        t = '$#' + '#'.join(s) + '#_'
        p = [0] * 4010
        mx, id, mmax, right = 0, 0, 0, 0
        for i in range(1, len(t) - 1):
            if mx > i:
                p[i] = min(p[2 * id - i], mx - i)
            else:
                p[i] = 1
            while t[i + p[i]] == t[i - p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                mx = i + p[i]
                id = i
            if mmax < p[i]:
                mmax = p[i]
                right = i
        return s[right//2 - mmax//2: right//2 - mmax//2 + mmax - 1]

# debug
s = Solution()
print s.longestPalindrome('ASBAASBAAA')

