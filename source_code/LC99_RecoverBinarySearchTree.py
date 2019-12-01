# -*- coding: utf-8 -*-

"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""

from utils.construct_tree import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode):
        if not root.left and not root.right:
            return

        def inorder_traverse(node):
            if not node:
                return
            stack = [node]
            top = stack[-1]
            result = []
            while stack:
                while top.left:
                    stack.append(top.left)
                    top = top.left
                pop_head = stack.pop(-1)
                result.append(pop_head)
                if pop_head.right:
                    stack.append(pop_head.right)
                    top = stack[-1]
            return result

        inorder_traverse_list = inorder_traverse(root)

        werid_index_1, werid_index_2 = 0, 0
        for i in range(0, len(inorder_traverse_list) - 1):
            if inorder_traverse_list[i].val > inorder_traverse_list[i + 1].val:
                werid_index_1 = i
                break
        for j in range(len(inorder_traverse_list)-1, 0, -1):
            if inorder_traverse_list[j].val < inorder_traverse_list[j - 1].val:
                werid_index_2 = j
                break

        inorder_traverse_list[werid_index_1].val, inorder_traverse_list[werid_index_2].val = inorder_traverse_list[
                                                                                                 werid_index_2].val, \
                                                                                             inorder_traverse_list[
                                                                                                 werid_index_1].val
