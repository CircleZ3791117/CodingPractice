#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''

'''
Solution: using DFS
'''

# Definition for a binary tree node
class TreeNode(object):
	def __init__(self, x):
		self.left = None
		self.right = None
		self.val = x

class Solution:
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rytype int
		"""
		if root == None:
			return 0
		i = 1
		res = []
		def dfs(root, res, i):
			if root == None:
				return
			if len(res) < i:
				res.append(i)
			dfs(root.left, res, i+1)
			dfs(root.right, res, i+1)
		dfs(root, res, i)
		return res[-1]

'''
Solution: BFS
'''
class Solution:
	def maxDepth(self, root):
		if root == None:
			return 0
		queue = []
		layers = 0
		queue.append(root)
		while(len(queue) != 0):
			tmp = []
			while(len(queue) != 0):
				head = queue.pop(0)
				if head.left != None:
					tmp.append(head.left)
				if head.right != None:
					tmp.append(head.right)
			queue = tmp
			layers += 1
		return layers

'''
Better Solution: one line
'''
class Solution(object):
	def maxDepth(self, root):
		return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0



