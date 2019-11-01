#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlez'

'''
Description:
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
'''

class Solution(object):
	def toLowerCase(self, str):
		"""
		:type str: str
		:rtype: str
		"""
		result = ''
		for c in str:
			if 65 <= ord(c) <= 90:
				result += chr(ord(c)+32)
			else:
				result += c
		return result


# One line solution using ''.join() for str

class Solution(object):
	def toLowerCase(self, str):
		return ''.join(chr(ord(c) - ord('A') + ord('a')) if ord('A') <= ord(c) <= ord('Z') else c for c in str)