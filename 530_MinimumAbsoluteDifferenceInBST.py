#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
'''
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def getMinimumDifference(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		mid_list = []
		mid_list = self.mid_traverse_list(root, mid_list)
		diff_list = []
		for i in range(len(mid_list)-1):
			diff_list.append(mid_list[i+1] - mid_list[i])
		return min(diff_list)

	def mid_traverse_list(self, node, mid_list):
		if node == None:
			return mid_list
		mid_list = self.mid_traverse_list(node.left, mid_list)
		mid_list.append(node.val)
		mid_list = self.mid_traverse_list(node.right, mid_list)
		return mid_list

