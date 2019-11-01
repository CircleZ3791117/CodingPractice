#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Description:

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
	def isPalindrome(self, x: int) -> bool:
		s = str(x)
		s_reverse = s[::-1]
		if s == s_reverse:
			return True
		else:
			return False

# Solve it without changing the integer to a string
class Solution2:
	def isPalindrome(self, x: int) -> bool:
		tmp = x
		if tmp < 0:
			return False
		if tmp == 0:
			return True
		reverse_value = 0
		while tmp:
			reverse_value = reverse_value * 10 + tmp % 10
			tmp = tmp // 10
		if reverse_value == x:
			return True
		else:
			return False

