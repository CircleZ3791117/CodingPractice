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

    def isSymmetric3(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        left_queue = [root.left]
        right_queue = [root.right]
        while left_queue and right_queue:
            lq_head = left_queue.pop(0)
            rq_head = right_queue.pop(0)
            if not lq_head and not rq_head:
                continue
            if not lq_head or not rq_head:
                return False
            if lq_head.val != rq_head.val:
                return False
            left_queue.append(lq_head.left)
            left_queue.append(lq_head.right)
            right_queue.append(rq_head.right)
            right_queue.append(rq_head.left)
        return True


