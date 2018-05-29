#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''
# Definition for a binary tree node
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSameTree(self, p, q):
		"""
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		if p == None and q == None:
			return True
		if p == None or q == None:
			return False
		p_list = []
		q_list = []
		p_list = self.serializeToList(p, p_list)
		q_list = self.serializeToList(q, q_list)
		if self.check_equal(p_list, q_list):
			return True
		return False

	def serializeToList(self, node, node_list):
		node_list.append(node.val)
		if node.left == None and node.right == None:
			return node_list
		if node.left:
			node_list = self.serializeToList(node.left, node_list)
		else:
			node_list.append('null')
		if node.right:
			node_list = self.serializeToList(node.right, node_list)
		return node_list

	def check_equal(self, a, b):
		if len(a) == len(b):
			for i in range(len(a)):
				if a[i] != b[i]:
					return False
			return True
		return False


# Simplify the code
class Solution(object):
	def isSameTree(self, p, q):
		"""
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		if p and q:
			return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
		return p is q

