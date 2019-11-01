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

## Approach #1 Using HashSet[Accepted]
'''
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
############################################################################

############################################################################
## Approach #2 Using BFS and HashSet

'''
In this approach, the idea of using the set is the same as in the last approach. But, we can carry on the traversal in a Breadth First Search manner, which is a very common traversal method used in Trees. The way BFS is used can be summarized as given below. We start by putting the root node into a queue. We also maintain a set similar to the last approach. Then, at every step, we do as follows:

1. Remove an element, p, from the front of the queue.

2. Check if the element k-p already exists in the set. If so, return True.

3. Otherwise, add this element, p to the set. Further, add the right and the left child nodes of the current node to the back of the queue.

4. Continue steps 1. to 3. till the queue becomes empty.

5. Return false if the queue becomes empty.

By following this process, we traverse the tree on a level by level basis.
'''

class Solution:
	def findTarget(self, root, k):
		"""
		:type root: Node
		:type k: int
		:rtype: bool
		"""
		if root == None:
			return False
		value_set = set()
		node_queue = list()
		node_queue.append(root)
		while node_queue:
			head = node_queue.pop(0)
			if k - head.val in value_set:
				return True
			else:
				value_set.add(head.val)
			if head.left:
				node_queue.append(head.left)
			if head.right:
				node_queue.append(head.right)
		return False

# test
initial_list = [5,3,6,2,4,None,7]
node_list = [TreeNode(value) for value in initial_list]
for i in xrange(len(node_list)/2 - 1):
	node_list[i].left = node_list[2 * i + 1]
	node_list[i].right = node_list[2 * i + 2]
	i += 1

s = Solution()
result = s.findTarget(node_list[0], 9)
print(result)

'''
Complexity Analysis

Time complexity : O(n)O(n). We need to traverse over the whole tree once in the worst case. Here, nn refers to the number of nodes in the given tree.

Space complexity : O(n)O(n). The size of the setset can grow atmost upto nn.
'''
############################################################################

############################################################################
## Approach #3 Using BST [Accepted]
'''
In this approach, we make use of the fact that the given tree is a Binary Search Tree. Now, we know that the inorder traversal of a BST gives the nodes in ascending order. Thus, we do the inorder traversal of the given tree and put the results in a list which contains the nodes sorted in ascending order.

Once this is done, we make use of two pointers l and r pointing to the beginning and the end of the sorted list. Then, we do as follows:

1. Check if the sum of the elements pointed by l and r is equal to the required sum k. If so, return a True immediately.

2. Otherwise, if the sum of the current two elements is lesser than the required sum k, update l to point to the next element. This is done, because, we need to increase the sum of the current elements, which can only be done by increasing the smaller number.

3. Otherwise, if the sum of the current two elements is larger than the required sum k, update r to point to the previous element. This is done, because, we need to decrease the sum of the current elements, which can only be done by reducing the larger number.

4. Continue steps 1. to 3. till the left pointer l crosses the right pointer r.

5. If the two pointers cross each other, return a False value.

Note that we need not increase the larger number or reduce the smaller number in any case. This happens because, in case, a number larger than the current list[r] is needed to form the required sum k, the right pointer could not have been reduced in the first place. The similar argument holds true for not reducing the smaller number as well.
'''

class Solution(object):
	def findTarget(self, root, k):
		if root == None:
			return False
		mid_order_list = []
		mid_order_list = self.midOrderTree(root, mid_order_list)
		mid_order_list_val = [node.val for node in mid_order_list]
		l = 0
		r = len(mid_order_list_val) - 1
		while l < r:
			sum_of_lr = mid_order_list_val[l] + mid_order_list_val[r]
			if  sum_of_lr == k:
				return True
			elif sum_of_lr < k:
				l += 1
			else:
				r -= 1
		return False


	def midOrderTree(self, root, mid_order_list):
		if root == None:
			return mid_order_list
		mid_order_list = self.midOrderTree(root.left, mid_order_list)
		mid_order_list.append(root)
		mid_order_list = self.midOrderTree(root.right, mid_order_list)
		return mid_order_list



