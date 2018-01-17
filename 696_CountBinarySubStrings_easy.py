# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''
'''
Solution
'''
class Solution:
	def countBinarySubstrings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		#print('target:{}'.format(s))
		count = 0
		for i, c in enumerate(s):
			if i == len(s)-1:
				break
			j = i+1
			step1 = 0
			while(j < len(s) and s[j] == c):
				step1 += 1
				j += 1
			#print('step1:{}'.format(step1))
			if j + step1 < len(s):
				result = sum(int(i) for i in s[j:j+step1+1])
				if result == 0 or result == step1+1:
					count += 1
			#print('c:{},i:{},count:{}'.format(c, i, count)
		print(count)
		return count

# test 10101
s = Solution()
s.countBinarySubstrings('00110')



