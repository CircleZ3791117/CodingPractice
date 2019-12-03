# -*- coding: utf-8 -*-

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

from utils.construct_tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return
        queue = [root]
        result_list = []
        while queue:
            level_num = len(queue)
            sub_list = []
            i = 0
            while i < level_num:
                head_node = queue.pop(0)
                if head_node.left:
                    queue.append(head_node.left)
                if head_node.right:
                    queue.append(head_node.right)
                sub_list.append(head_node.val)
                i += 1
            result_list.append(sub_list)
        return result_list
