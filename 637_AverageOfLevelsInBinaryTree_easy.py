# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''

class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution:
	def averageOfLevels(self, root):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""
		if root==None:
			return
		results = []
				
	
			

# Your input
# [3,9,20,15,7]
# Your answer
# [3,14.50000]
# Expected answer
# [3.00000,14.50000,11.00000]



