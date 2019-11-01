#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X. A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
'''

class Solution(object):
	def rotatedDigits(self, N):
		"""
		:type N: int
		:rtype: int
		"""
		count = 0
		GNUMBER = [0, 1, 2, 5, 6, 8, 9]
		GNUMBER_CHANGE = [2, 5, 6, 9]
		for i in xrange(1, N+1):
			str_i = str(i)
			if all(int(item) in GNUMBER for item in str_i) and any(int(item) in GNUMBER_CHANGE for item in str_i):
				count += 1
		return count
