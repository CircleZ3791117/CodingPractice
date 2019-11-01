#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
'''

'''
Solution: recursive method
'''

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		if root == None:
			return
		tmp = root.left
		root.left = root.right
		root.right = tmp
		self.invertTree(root.left)
		self.invertTree(root.right)
		return root

class Solution(object):
	def invertTree(self, root):
		if root == None:
			return
		if root.left == None and root.right == None:
			return root
		left = self.invertTree(root.left)
		right = self.invertTree(root.right)
		root.left = right
		root.right = left
		return root

'''
Solution: no recursive method, using queue(similar to BFS)
'''
class Solution:
	def invertTree(self, root):
		if root == None:
			return
		if root.left == None and root.right == None:
			return root
		queue = []
		queue.append(root)
		while(len(queue) != 0):
			tmp = []
			while(len(queue) != 0):
				head = queue.pop(0)
				if head.left != None: tmp.append(head.left)
				if head.right != None: tmp.append(head.right)
				if head.left != None or head.right != None:
					t = head.left
					head.left = head.right
					head.right = t
			queue = tmp
		return root

'''
Better Solution: using the a, b = b, a syntax of python to swap two object
'''
# recursive
class Solution:
	def invertTree(self, root):
		if root:
			root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
			return root

# iterative
class Solution:
	def invertTree(self, root):
		stack = [root]
		while stack:
			head = stack.pop()
			if head:
				head.left, head.right = head.right, head.left
				stack += head.left, head.right
		return root

'''
Extension: pre-order, in-order, post-order.

Interesting. Your iterative solution is iterative in-order DFS, and @StefanPochmann 's version is iterative pre-order DFS, while I first thought about iterative post-order DFS as an attempt of direct translation of the short recursive post-order. Apparently, all three versions work for this problem. In the recursive world, those would be:
'''
# Pre-order
if not root:
    return root
root.left, root.right = root.right, root.left
self.invertTree(root.left)
self.invertTree(root.right)
return root

# In-order
if not root:
    return root
self.invertTree(root.left)
root.left, root.right = root.right, root.left
self.invertTree(root.left)
return root

# Post-order (this is the longer version of @StefanPochmann 's first solution)
if not root:
    return root
self.invertTree(root.left)
self.invertTree(root.right)
root.left, root.right = root.right, root.left
return root

'''
The first two recursive solutions don’t allow for recursive calls to be compressed into one line, but post-order version does, so it is preferable.

Since in-, pre- and post-order recursive traversals can all be converted into their respective iterative forms, any one of those will work, but from the iterative implementation logic pre-order is easier than in-order and in-order is in turn easier than post-order, so if we need an iterative solution, it would make sense for us to choose the iterative pre-order in an interview, which Stefan did here in his explicit stack solution. I personally prefer though to maintain an invariant of no None’s in the stack, since it saves on number of append calls and while loop iterations at the expense of if checks which are cheaper, so I usually do this:
'''

if not root:
    return None
stack = [root]
while stack:
    node = stack.pop()
    node.left, node.right = node.right, node.left  #specific to this problem
    if node.right:
        stack.append(node.right)
    if node.left:
        stack.append(node.left)
return root

'''



