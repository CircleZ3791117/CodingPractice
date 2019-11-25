# -*- coding: utf-8 -*-

'''Utils for Tree Problem'''

import logging

logging.basicConfig(level=logging.INFO)


class TreeNode:
    """
    Tree node definition.
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def get_node_val(self):
        return self.val


class BinaryTree:
    """
    Binary tree definition.
    """

    def __init__(self, val_list):
        self.root = self.build_binary_tree_from_an_incomplete_val_sequence(val_list)

    def build_binary_tree(self, val_list):
        """Build Tree from list of node values from complete trees.

        # Arguments
        val_list: list, node value list

        # Return
        root of binary tree
        """
        if len(val_list) < 1:
            logging.error("List is empty, unable to build binary tree.")
            return
        node_list = val_list.copy()
        for i in range(len(node_list)):
            if node_list[i] == 'null':
                node_list[i] = None
            else:
                node_list[i] = TreeNode(node_list[i])
        root = node_list[0]
        i = 0
        while i <= len(node_list) / 2 - 1:
            if node_list[i]:
                node_list[i].left = node_list[2 * i + 1]
                node_list[i].right = node_list[2 * i + 2]
            i += 1
        return root

    def build_binary_tree_from_an_incomplete_val_sequence(self, val_list):
        if len(val_list) < 1:
            logging.error("List is empty, unable to build binary tree.")
            return
        node_list = [TreeNode(val_list[0])]
        i = 1
        node_index = 0
        while i < len(val_list):
            if val_list[i] != "null":
                new_node = TreeNode(val_list[i])
                node_list[node_index].left = new_node
                node_list.append(new_node)
            i += 1
            if i == len(val_list):
                break
            if val_list[i] != "null":
                new_node = TreeNode(val_list[i])
                node_list[node_index].right = new_node
                node_list.append(new_node)
            i += 1
            node_index += 1
        return node_list[0]

    def pre_order_traverse(self):
        if not self.root:
            logging.error("root of btree should not be empty.")
            return
        btree_node_list = list()

        def pre_recur(node, node_list):
            if not node:
                return
            node_list.append(node)
            pre_recur(node.left, node_list)
            pre_recur(node.right, node_list)

        pre_recur(self.root, btree_node_list)

        val_list = list()
        for item in btree_node_list:
            val_list.append(item.val)
        return val_list

    def in_order_traverse(self):
        if not self.root:
            logging.error("root of btree should not be empty.")
            return
        btree_node_list = list()

        def in_recur(node, node_list):
            if not node:
                return
            in_recur(node.left, node_list)
            node_list.append(node)
            in_recur(node.right, node_list)

        in_recur(self.root, btree_node_list)

        val_list = list()
        for item in btree_node_list:
            val_list.append(item.val)
        return val_list

    def after_order_traverse(self):
        if not self.root:
            logging.error("root of btree should not be empty.")
            return
        btree_node_list = list()

        def after_recur(node, node_list):
            if not node:
                return
            after_recur(node.left, node_list)
            after_recur(node.right, node_list)
            node_list.append(node)

        after_recur(self.root, btree_node_list)

        val_list = list()
        for item in btree_node_list:
            val_list.append(item.val)
        return val_list
