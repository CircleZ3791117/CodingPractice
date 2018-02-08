#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.
'''
from operator import xor

class Solution:
	def getSum(self, a, b):
		"""
		:type a: int
		:type b: int
		:rtype: int
		"""
		result = []
		bin_a_reverse = bin(a)[2:][::-1]
		bin_b_reverse = bin(b)[2:][::-1]
		
		
	




s = Solution()
s.getSum(6, 2)

