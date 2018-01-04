# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
because "aba" is a subsequence of "aba", 
but not a subsequence of any other strings in the group of two strings. 
Note:

Both strings' lengths will not exceed 100.
Only letters from a ~ z will appear in input strings.
'''

'''
Solution
'''
class Solution:
	def findLUSlength(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: int
		"""
		if len(a) == 0 and len(b) == 0:
			return -1
		if len(a) != len(b):
			return len(a) if len(a)>len(b) else len(b)
		else:
			return False


'''
Better Solution
'''
class Solution:
	def findLUSlength(self, a, b):
		return -1 if a==b else max(len(a), len(b))



















>>>>>>> 3fdef1177c539372e149e7158d95b31b14852810
