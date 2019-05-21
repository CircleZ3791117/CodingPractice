#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Description:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
	def longestPalindrome(self, s: str)->str:
		if len(s) <= 0:
			return ""
		i = 0
		j = len(s) - 1
		longest_palindrome = 0
		result = ""

		while i < len(s):
			tmp_length = 0
			tmp_result  = ""
			while j >= i:
				if j - i + 1 < longest_palindrome:
					break 
				if s[i] != s[j]:
					j -= 1
				else:
					if self.judge_palin(s, i, j):
						l = j - i + 1
						tmp_length = l
						if j == len(s) - 1:
							tmp_result += s[i:]
						else:
							tmp_result += s[i:j+1]
						break
					j -= 1
			if tmp_length > longest_palindrome:
				longest_palindrome = tmp_length
				result = tmp_result
			i += 1
			j = len(s) - 1
		return result

	def judge_palin(self, s, i, j):
		flag = True
		while i < j:
			if s[i] == s[j]:
				i += 1
				j -= 1
			else:
				flag = False
				return flag
		return flag

		
