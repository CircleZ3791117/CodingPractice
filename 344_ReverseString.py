#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''

'''
Solution
Little reverse tricks
'''
class Solution:
	def reverseString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		return s[::-1]