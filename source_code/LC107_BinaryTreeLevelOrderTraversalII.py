# -*- coding: utf-8 -*-

"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

from utils.construct_tree import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root:
            return

        queue = [root]
        result_list = []

        while queue:
            level_num = len(queue)
            i = 0
            sub_list = []
            while i < level_num:
                head_queue = queue.pop(0)
                sub_list.append(head_queue.val)
                if head_queue.left:
                    queue.append(head_queue.left)
                if head_queue.right:
                    queue.append(head_queue.right)
                i += 1
            result_list.append(sub_list)

        def reverse_list(rlist):
            if len(rlist) < 1:
                return
            i = 0
            j = len(rlist) - 1
            while i < j:
                rlist[i], rlist[j] = rlist[j], rlist[i]
                i += 1
                j -= 1

        reverse_list(result_list)
        return result_list
