# -*- coding: utf-8 -*-

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

from utils.construct_tree import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        if not root:
            return True
        stack = [root]
        top = stack[-1]
        while stack:
            while top.left:
                stack.append(top.left)
                top = top.left
            pop_node = stack.pop(-1)
            if not len(result):
                result.append(pop_node.val)
            elif pop_node.val > result[-1]:
                result.append(pop_node.val)
            else:
                return False
            if pop_node.right:
                stack.append(pop_node.right)
                top = stack[-1]
        return True
