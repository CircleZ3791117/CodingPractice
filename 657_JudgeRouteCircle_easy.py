# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''

'''
Solution:
use (x,y) to represent the position, R:x+1, L:x-1, U:y+1, D:y-1
'''
class Solution:
	def judgeCircle(self, moves):
		"""
		:type moves: str
		:rtype: bool
		"""
		moves_str = moves
		x, y = (0, 0)
		for m in moves_str:
			if m == 'R':
				x = x + 1
			elif m == 'L':
				x = x - 1
			elif m == 'U':
				y = y + 1
			elif m == 'D':
				y = y - 1
			else:
				raise ValueError('Invalid move')
		if x==0 and y==0:
			return True
		return False

'''
Better Solution
'''
class Solution:
	def judgeCircle(self, moves):
		return moves.count('R')==moves.count('L') and moves.count('U')==moves.count('D')
