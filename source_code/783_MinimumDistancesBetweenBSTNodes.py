#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
'''

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def minDiffInBST(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		mid_list = []
		diff_list = []
		mid_list = self.mid_traverse_BST(root, mid_list)
		for i in range(len(mid_list)-1):
			diff_list.append(abs(mid_list[i] - mid_list[i+1]))
		return min(diff_list)

	def mid_traverse_BST(self, root, mid_list):
		if not root:
			return mid_list
		if root.left:
			self.mid_traverse_BST(root.left, mid_list)
		mid_list.append(root.val)
		if root.right:
			self.mid_traverse_BST(root.right, mid_list)
		return mid_list

# Using stack
class Solution(object):
	def minDiffInBST(self, root):
		if not root:
			return
		mid_list = []
		diff_list = []
		stack = []
		node = root
		while node or stack:
			while node:
				stack.append(node)
				node = node.left
			if stack:
				top = stack.pop()
				mid_list.append(top.val)
				node = top.right
		for i in range(len(mid_list) - 1):
			diff_list.append(abs(mid_list[i]-mid_list[i+1]))
		return min(diff_list)
