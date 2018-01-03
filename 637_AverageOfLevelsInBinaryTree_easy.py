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

'''
Solution
'''

# DFS

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
		res = []
		count = []
		self.average(root, i, res, count)
		return [res[i]*1.0/count[i] for i in range(len(res))]

	def average(self, root, i, res, count):
		if root == None:
			return
		if i < len(res):
			res[i] += root.val
			count[i] += 1
		else:
			res.append(root.val)
			count.append(1)	
		self.average(root.right, i+1, res, count)
		self.average(root.left, i+1, res, count)		
	
# BFS
class Solution:
	def averageOfLevels(self, root):
		queue = []
		res = []
		queue.append(root)
		while(len(queue)!=0):
			sum = 0
			count = 0
			tmp = []
			while(len(queue)!=0):
				sum += queue[0].val
				count += 1
				item = queue.pop(0)
				if item.left != None:
					tmp.append(item.left)
				if item.right != None:
					tmp.append(item.right)
			queue = tmp
			res.append(sum*1.0 / count)
		return res

				



