# -*- coding: utf-8 -*-

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
    3   3


Note:
Bonus points if you could solve it both recursively and iteratively.
"""

from utils.construct_tree import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def is_equal(lnode, rnode):
            if not lnode and not rnode:
                return True
            if not lnode or not rnode:
                return False
            if lnode.val == rnode.val:
                return is_equal(lnode.left, rnode.right) and is_equal(lnode.right, rnode.left)

        return is_equal(root.left, root.right)

    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = [root, root]

        while queue:
            fhead = queue.pop(0)
            shead = queue.pop(0)
            if not fhead and not shead:
                continue
            if not fhead or not shead:
                return False
            if fhead.val != shead.val:
                return False
            queue.append(fhead.left)
            queue.append(shead.right)
            queue.append(fhead.right)
            queue.append(shead.left)

        return True




