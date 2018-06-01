#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

class Solution(object):
	def sumOfLeftLeaves(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		left_leaves_list = []
		left_leaves_list = self.first_traverse(root, left_leaves_list)
		return sum(left_leaves_list)


	def first_traverse(self, node, left_leaves_list):
		if node == None:
			return left_leaves_list
		if node.left:
			left_leaves_list.append(node.left.val)
			self.first_traverse(node.left, left_leaves_list)
		if node.right:
			self.first_traverse(node.right, left_leaves_list)
