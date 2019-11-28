# -*- coding: utf-8 -*-

'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

from utils.construct_tree import TreeNode


class Solution:
    def get_trees_recur(self, left, right):
        node_list = list()
        if left > right:
            return [None]
        if left == right:
            return [TreeNode(left)]
        i = left
        while i <= right:
            left_node_list = self.get_trees_recur(left, i - 1)
            right_node_list = self.get_trees_recur(i + 1, right)
            for lnode in left_node_list:
                for rnode in right_node_list:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    node_list.append(root)
            i += 1
        return node_list

    def generateTrees(self, n: int) -> list:
        if n < 1:
            return
        return self.get_trees_recur(1, n)


