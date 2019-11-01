#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

class Solution(object):
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		map_t_n = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
		summarize = 0
		for i in range(len(s)):
			summarize += map_t_n[s[i]] * pow(26, len(s)-i-1)
		return summarize

'''
Better Solution(elegant and beautiful)
'''
class Solution(object):
	def titleToNumber(self, s):
		return reduce(lambda x, y: 26 * x + y, [ord[c]-64 for c in s])