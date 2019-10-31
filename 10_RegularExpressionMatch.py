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
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

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
		i = 0
		j = 0
		while i < len(s) and j < len(p):
			if s[i] == p[j] or p[j] == '.':
				i += 1
				if j+1 < len(p) and p[j+1] != '*':
					j += 1
				if j+1 >= len(p):
					j += 1
			else:
				if j+1 < len(p) and p[j+1] == '*':
					j += 2
		if i == len(s):
			return True
		else:
			return False


import unittest
class SolutionTestCase(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(SolutionTestCase, self).__init__(*args, *kwargs)
		self.test_solution = Solution()

	@classmethod
	def setUpClass(cls):
		print("setUpClass")

	@classmethod
	def tearDownClass(cls):
		print("tearDownClass")

	def setUp(self):
		print("--setUp--")

	def tearDown(self):
		print("--tearDown--")

	def test_isMatch(self):
		print("test isMatch()...")
		self.assertEqual(False, self.test_solution.isMatch('aa', 'a'))
		self.assertEqual(True, self.test_solution.isMatch('aa', 'aa'))


if __name__ == "__main__":
	unittest.main()


			




