#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R    
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
PAHNAPLLSIIIGGYIR
PAHNAPLSIIGYIR
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R   
P     I     
"""
	
class Solution:
	def convert(self, s:str, numRows:int)->str:
		if numRows <= 1:
			return s
		if len(s) <= numRows:
			return s
		i = 0 
		result = []
		d = numRows + numRows - 2
		for i in range(numRows):
			j = i
			if j == 0 or j == numRows - 1:
				while j < len(s):
					result.append(s[j])
					j += d
				i += 1
			else:
				distance1 = d - 2 * j
				distance2 = d - distance1
				result.append(s[j])
				while j < len(s):	
					j += distance1
					if j < len(s):
						result.append(s[j])
					else:
						i += 1
						break
					j += distance2
					if j < len(s):
						result.append(s[j])
					else:
						i += 1
						break
				i += 1
		result = ''.join(result)
		return result





