#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'CZ'


"""
Description:
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		len_s = len(s)
		len_p = len(p)
		i = 0
		j = 0
		while i < len_s and j < len_p:
			if s[i] == p[j] or p[j] == '.':
				i += 1
				j += 1
			elif s[i] != p[j] and p[j] == '*' and j-1 >= 0 and (p[j-1]==s[i] or p[j-1]=='.'):
				i += 1
			elif s[i] != p[j] and p[j] != '*' and j+2 < len_p and p[j+1] == '*':
				j += 2
			else:
				return False
		if i == len_s:
			if j < len_p:
				while j < len_p:
					if p[j] == '*':
						j += 1
					elif p[j] != '*' and j+1 < len_p and p[j+1] == '*':
						j += 2
					else:
						return False
				return True
			else:
				return True
		else:
			return False
			




