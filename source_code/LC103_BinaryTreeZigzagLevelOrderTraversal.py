# -*- coding: utf-8 -*-

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

from utils.construct_tree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return
        queue = [root]
        result_list = []
        while queue:
            level_num = len(queue)
            sub_list = []
            i = 0
            while i < level_num:
                head_queue = queue.pop(0)
                sub_list.append(head_queue.val)
                if head_queue.left:
                    queue.append(head_queue.left)
                if head_queue.right:
                    queue.append(head_queue.right)
                i += 1
            result_list.append(sub_list)

        def reverse_list(val_list):
            if len(val_list) < 1:
                return
            i = 0
            j = len(val_list) - 1
            while i < j:
                val_list[i], val_list[j] = val_list[j], val_list[i]
                i += 1
                j -= 1
            return val_list

        i = 1
        while i < len(result_list):
            if i % 2 == 1:
                result_list[i] = reverse_list(result_list[i])
            i += 1
        return result_list
