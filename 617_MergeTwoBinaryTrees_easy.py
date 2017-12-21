# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

Note: The merging process must start from the root nodes of both trees.
'''

'''
Solution
Merge two trees recursively
'''

# Definition for a binary tree node
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.rigt = None

class Solution(object):
	def mergeTrees(self, t1, t2):
		"""
		:type t1: TreeNode
		:type t2: TreeNode
		:rtype: TreeNode
		"""
		if t1 != None and t2 != None:
			val = t1.val + t2.val
			new_t = TreeNode(val)
			new_t.left = self.mergeTrees(t1.left, t2.left)
			new_t.right = self.mergeTrees(t1.right, t2.right)
		elif t1 != None and t2 == None:
			new_t = t1
		elif t1 ==None and t2 != None:
			new_t = t2
		else:
			return None
		
		return new_t


'''
Better Solution
'''

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """      
        if t1 is None:
           return t2
    
        if t2 is None:
           return t1
    
        if t1 != None and t2 != None:
           t1.val += t2.val
           t1.left = self.mergeTrees(t1.left, t2.left)
           t1.right = self.mergeTrees(t1.right, t2.right) 
        
        return t1  