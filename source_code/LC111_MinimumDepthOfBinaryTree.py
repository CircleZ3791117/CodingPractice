# -*- coding: utf-8 -*-

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

from utils.construct_tree import TreeNode

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = 1
        queue = [root]
        while queue:
            level_num = len(queue)
            i = 0
            while i < level_num:
                head_queue = queue.pop(0)
                if head_queue.left:
                    queue.append(head_queue.left)
                if head_queue.right:
                    queue.append(head_queue.right)
                if not head_queue.left and not head_queue.right:
                    return level
                i += 1
            level += 1
