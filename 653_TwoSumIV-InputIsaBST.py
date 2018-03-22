#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''

# Definition for a binary tree node
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findTarget(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: bool
		"""
		node_list = []
		node_list = self.getAllTreeNode(root, node_list)
		for i in xrange(len(node_list)):
			if (k - node_list[i]) in (node_list[0:i] + node_list[i+1:]):
				return True
		return False

	def getAllTreeNode(self, root, node_list):
		if root == None:
			return
		node_list.append(root.val)
		self.getAllTreeNode(root.left, node_list)
		self.getAllTreeNode(root.right, node_list)
		return node_list

'''
Better Solution
'''

'''
Approach #1 Using HashSet[Accepted]
The simplest solution will be to traverse over the whole tree and consider every possible pair of nodes to determine if they can form the required sum k. But, we can improve the process if we look at a little catch here.

If the sum of two elements x+y equals k, and we already know that x exists in the given tree, we only need to check if an element y exists in the given tree, such that y = k - x. Based on this simple catch, we can traverse the tree in both the directions(left child and right child) at every step. We keep a track of the elements which have been found so far during the tree traversal, by putting them into a set.

For every current node with a value of p, we check if k−p already exists in the array. If so, we can conclude that the sum k can be formed by using the two elements from the given tree. Otherwise, we put this value p into the set.

If even after the whole tree's traversal, no such element p can be found, the sum k can't be formed by using any two elements.
'''
class Solution:
	def findTarget(self, root, k):
		store = set()
		return self.recursiveFindTarget(root, k, store)

	def recursiveFindTarget(self, root, k, store):
		if root == None:
			return False
		if (k - root.val) in store:
			return True
		store.add(root.val)
		return self.recursiveFindTarget(root.left, k, store) | self.recursiveFindTarget(root.right, k, store)

'''
Complexity Analysis

Time complexity : O(n). The entire tree is traversed only once in the worst case. Here, n refers to the number of nodes in the given tree.

Space complexity : O(n). The size of the setset can grow upto nn in the worst case.
'''










