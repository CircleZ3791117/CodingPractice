#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "CZ"

"""
Description:

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""

# Definition of a binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def rangeSumBST(self, root, L, R):
		"""
		:type root: TreeNode
		:type L: int
		:type R: int
		:rtype: int
		"""
		mid_list = []
		node = root
		stack = []
		while node or stack:
			while node:
				stack.append(node)
				node = node.left
			if stack:
				top = stack.pop()
				mid_list.append(top.val)
				node = top.right
		sum = 0
		for item in mid_list:
			if item >= L and item <= R:
				sum += item
		return sum

# Recursive method
class Solution:
	def rangeSumBST(self, root, L, R):
		def dfs(node):
			if node:
				if L <= node.val <= R:
					self.ans += node.val
				# Be carefule of the conditions below
				if L < node.val:
					dfs(node.left)
				if R > node.val:
					dfs(node.right)
		self.ans = 0
		dfs(root)
		return self.ans

# Iterative method
class Solution:
	def rangeSumBST(self, root, L, R):
		node_list = [root]
		ans = 0
		while node_list:
			node = node_list.pop()
			if node:
				if L <= node.val <= R:
					ans += node.val
				if node.val < R:
					node_list.append(node.right)
				if node.val > L:
					node_list.append(node.left)
		return ans

