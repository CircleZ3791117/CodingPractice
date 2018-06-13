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
		root_bak = copy.deepcopy(root)
		stack.append(root_bak)
		while(stack):
			top = stack[-1]
			if top.left:
				stack.append(top.left)
				top.left = None
			else:
				tmp = stack.pop()
				mid_list.append(tmp.val)
				if tmp.right:
					stack.append(tmp.right)
		for i in range(len(mid_list)-1):
			diff_list.append(abs(mid_list[i] - mid_list[i+1]))
		return min(diff_list)

# After the love, 

# If you sit down and obesrve, you will find the panic in your heart. You can see things that you can't
# see than before. We feel lost somethimes because of losing beliefs. 

# What can i do for you? In the process of creation. The true love.

# we have keep poistive remember the most import time is now. The most important people is the people
# around you. You try to serve the human beings. If something is easy to get, than it is boring.
# Marriage has to be perfomed. When you can find and catch the details, but every time I get home, I
# can get a flower. I'm his girl friend. Why he knows nothing? She chose to back up. Two people love each
# other for 7 years. 

# This is what i know as love. I love to . Dao, the basic principles.

# Hello, every one , today we are talking about

# I came here the first time. The know things very well. You are the flowers under heart.

# Please give a big hug to your children after the exam.

# The first impression is very import. If i'm different from the world, then just let me be different. This
# Time just let this time be differ
