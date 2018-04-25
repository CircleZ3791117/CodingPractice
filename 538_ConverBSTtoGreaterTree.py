#!usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def convertBST(self, root):
		"""
		:root: TreeNode
		:rtype: TreeNode
		"""
		if not root:
			return
		mid_order_node_list = []
		mid_order_node_list = self.midOrderTree(root, mid_order_node_list)
		node_len = len(mid_order_node_list)
		# using cache
		sum_cache = [0] * node_len
		val_list = [node.val for node in mid_order_node_list]	
		j = -1
		sum_cache[-1] = val_list[-1]
		while(abs(j) <= node_len):
			j -= 1
			if abs(j) <= node_len:
				sum_cache[j] = sum_cache[j+1] + val_list[j]
		for i in xrange(node_len):
			mid_order_node_list[i].val = sum_cache[i]
		return root

		# for i in xrange(len(mid_order_node_list)):
		# 	mid_order_node_list[i].val = sum(node.val for node in mid_order_node_list[i:])
		# return root

	def midOrderTree(self, root, mid_order_node_list):
		if root == None:
			return mid_order_node_list
		self.midOrderTree(root.left, mid_order_node_list)
		mid_order_node_list.append(root)
		self.midOrderTree(root.right, mid_order_node_list)
		return mid_order_node_list


'''
Algorithm

For the recursive approach, we maintain some minor "global" state so each recursive call can access and modify the current total sum. Essentially, we ensure that the current node exists, recurse on the right subtree, visit the current node by updating its value and the total sum, and finally recurse on the left subtree. If we know that recursing on root.right properly updates the right subtree and that recursing on root.left properly updates the left subtree, then we are guaranteed to update all nodes with larger values before the current node and all nodes with smaller values after.
'''




