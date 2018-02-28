#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.
'''

'''
Solution
'''
class Solution:
	def letterCasePermutation(self, S):
		"""
		:type S: str
		:rtype: List[str]
		"""
		result = []
		if S is None:
			return result
		result.append(S)
		tmp = str()
		for i in S:
			if ord(i) >= 65 and ord(i) <= 90:
				tmp += chr(ord(i) + 32)
			if ord(i) >= 97 and ord(i) <= 122:
				tmp += chr(ord(i) - 32)
			tmp += i
		result.append(tmp)
		return result


