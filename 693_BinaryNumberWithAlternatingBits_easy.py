#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
'''

'''
Solution
'''
class Solution:
	def hasAlternatingBits(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		binary_n = bin(n)[2:]
		for i in range(len(binary_n)-1):
			if binary_n[i] == binary_n[i+1]:
				return False
		return True


'''
Better Solution
'''
class Solution:
	def hasAlternatingBits(self, n):
		while(n!=0):
			cur = n % 2
			n = n / 2
			if cur == n % 2:
				return False
		return True






