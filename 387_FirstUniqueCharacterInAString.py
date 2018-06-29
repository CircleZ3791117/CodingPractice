#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

"""
Description:
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		char_list = []
		value_list = []
		for c in s:
			if c not in char_list:
				char_list.append(c)
				value_list.append(1)
			else:
				value_list[char_list.index(c)] += 1
		for i in range(len(value_list)):
			if value_list[i] == 1:
				return s.index(char_list[i])
		return -1
