#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
'''

class Solution(object):
	def isOneBitCharacter(self, bits):
		"""
		:type bits: List[int]
		:rtype: bool
		"""
		if len(bits) < 2:
			return True
		nums_of_1 = 0
		current_index = -2
		while(abs(current_index) <= len(bits)):
			if bits[current_index] == 0 and nums_of_1 % 2 == 0:
				return True
			if bits[current_index] == 0 and nums_of_1 % 2 == 1:
				return False
			if bits[current_index] == 1:
				nums_of_1 += 1
			current_index -= 1
		if nums_of_1 % 2 == 0:
			return True
		else:
			return False

## Super cool, the above method beats 100.00% of python3 submissions.
		
# A more elegant expression using Greedy
class Solution(object):
	def isOneBitCharacter(self, bits):
		"""
		:type bits: List[int]
		:rtype: bool
		"""
		parity = bits.pop()
		while bits and bits.pop(): parity ^= 1
		return parity == 0

