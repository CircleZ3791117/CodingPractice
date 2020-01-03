# -*- coding: utf-8 -*-

"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

from utils.construct_tree import TreeNode


class Solution(object):
    def rightSideView(self, root):
        """
        Return the right side view of a binary Tree.

        Args:
            root: TreeNode, the root of target binary tree.

        Returns:
            list(int), the values of nodes in the right side view.
        """
        if not root:
            return
        # Use BFS to traverse the tree level by level.
        queue = [root]
        result = []
        while queue:
            # Current level node number is equal to the length of queue.
            level_num = len(queue)
            tmp = []
            i = 0
            while i < level_num:
                head = queue.pop(0)
                tmp.append(head.val)
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
                i += 1
            result.append(tmp)

        right_view_value = []
        # The right view if the made up of last element in each level.
        for level in result:
            right_view_value.append(level[-1])
        return right_view_value



