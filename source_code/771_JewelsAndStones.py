#!usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''

class Solution:
	def numJewelsInStones(self, J, S):
		"""
		:type J: str
		:type S: str
		:rtype: int
		"""
		j_map = {}
		result = 0
		for i in J:
			j_map[i] = 1
		for i in S:
			if j_map.has_key(i):
				result += 1
		return result

'''
Better Solution
'''
class Solution:
	def numJewelsInStones(self, J, S):
		return sum(map(S.count, J))

class Solution:
	def numJewelsInStones(self, J, S):
		return sum(map(J.count, S))

class Solution:
	def numJewelsInsStones(self, J, S):
		return sum(s in J for s in S)