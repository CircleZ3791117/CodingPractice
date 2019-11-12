#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_cur = 0
        p_cur = 0
        star = -1
        match = 0
        while s_cur < len(s):
            if p_cur < len(p) and (p[p_cur] == s[s_cur] or p[p_cur] == '?'):
                s_cur += 1
                p_cur += 1
            elif p_cur < len(p) and p[p_cur] == '*':
                match = s_cur
                star = p_cur
                p_cur += 1
            elif star != -1:
                p_cur = star + 1
                match += 1
                s_cur = match
            else:
                return False

        while p_cur < len(p) and p[p_cur] == '*':
            p_cur += 1

        if p_cur == len(p):
            return True
        else:
            return False


# Using dynamic programming
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        # initialize dp matrix
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        j = 1
        while j < len(p) + 1:
            if p[j-1] != '*':
                break
            else:
                dp[0][j] = True
            j += 1
        i = 1
        while i < len(s) + 1:
            j = 1
            while j < len(p) + 1:
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
                j += 1
            i += 1
        return dp[len(s)][len(p)]