#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
'''
class Solution(object):
	def findComplement(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		binary_num = bin(num)
		result = []
		for i in binary_num[2:]:
			if i=='0':
				result.append('1')
			else:
				result.append('0')
		result_str = ''.join(result)
		return int(result_str, 2)

# test
# s = Solution()
# s.findComplement(5)

'''
Better Solution:
The key is how to construct 111...: use <<
'''
class Solution:
	def findComplement(self, num):
		one = 1
		while one <= num:
			# wrong: one << 1, would cause time limitted error
			one = one << 1
		return (one-1) ^ num
