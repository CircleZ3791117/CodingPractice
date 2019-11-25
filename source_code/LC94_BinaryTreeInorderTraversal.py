#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return

        result_list = []

        def in_oder_recur(node, node_list):
            if not node:
                return
            in_oder_recur(node.left, node_list)
            node_list.append(node.val)
            in_oder_recur(node.right, node_list)

        in_oder_recur(root, result_list)

        return result_list

    def inorder_traverse_nonrecursive(self, root: TreeNode) -> list:
        if not root:
            return
        node_stack = [root]
        result_list = []
        top = node_stack[-1]
        while len(node_stack) != 0:
            while top.left:
                node_stack.append(top.left)
                top = node_stack[-1]
            cur_top = node_stack[-1]
            result_list.append(node_stack.pop(-1).val)
            if cur_top.right:
                node_stack.append(cur_top.right)
                top = node_stack[-1]
        return result_list
