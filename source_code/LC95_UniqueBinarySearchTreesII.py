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
    def generateTrees(self, n: int) -> list:
        if n < 1:
            return

        def get_trees_recur(left, right):
            node_list = list()
            if left > right:
                return [None]
            i = left
            while i <= right:
                left_node_list = get_trees_recur(left, i - 1)
                right_node_list = get_trees_recur(i + 1, right)
                for lnode in left_node_list:
                    for rnode in right_node_list:
                        root = TreeNode(i)
                        root.left = lnode
                        root.right = rnode
                        node_list.append(root)
                i += 1
            return node_list

        return get_trees_recur(1, n)

    # Using DP
    def generate_trees_using_dp(self, n: int) -> list:
        if n < 1:
            return [None]

        # change node value by delta deeply
        def deep_copy(node, delta):
            if not node:
                return None
            delta_node = TreeNode(node.val + delta)
            delta_node.left = deep_copy(node.left, delta)
            delta_node.right = deep_copy(node.right, delta)
            return delta_node

        # define dp, each element represent the root list of all possible BST tree
        dp = [[] for _ in range(n + 1)]
        dp[0].append(None)
        for i in range(1, n + 1):
            for j in range(0, i):
                for lnode in dp[j]:
                    for rnode in dp[i - 1 - j]:
                        root = TreeNode(j + 1)
                        root.left = lnode
                        root.right = deep_copy(rnode, j + 1)
                        dp[i].append(root)

        return dp[n]
