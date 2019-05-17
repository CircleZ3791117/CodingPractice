#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Description:

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
	def reverse(self, x: int) -> int:
		s = str(x)
		flag = 1
		if s[0] == '-':
			s = s[1:]
			flag = -1
		s = s[::-1]
		result = 0
		l = len(s)
		for item in s:
			result += int(item) * pow(10, l-1)
			l -= 1
		result = result * flag
		if -pow(2, 31) <= result <= pow(2, 31) - 1:
			return result
		else:
			return 0

class Solution:
	def reverse(self, x: int) -> int:
		s = str(x)
		flag = 1
		print('test')
		if s[0] == '-':
			s = s[1:]
			flag = -1
		s = s[::-1]
		result = 0
		l = len(s)
		for item in s:
			result += int(item) * pow(10, l-1)
			l -= 1
		return result * flag

'''
Other methods
'''

# mathematical way, using long int to store result
class Solution:
	def reverse(self, x: int) -> int:
		sign = x >= 0
		if not sign:
			x = -x
		result = 0
		while x:
			result = result * 10 + x % 10
			x = x // 10
		if not sign:
			result = -result
		if result <= 2**31 - 1 and result >= -2**31:
			return result
		return 0 
