# -*- coding -*-
'''test tree utils'''

from utils.construct_tree import TreeNode, BinaryTree
import unittest


class TestTreenode(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTreenode, self).__init__(*args, **kwargs)
        self.node = TreeNode(1)

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class...")

    def setUp(self) -> None:
        print("set up")

    def tearDown(self) -> None:
        print("tear down")

    def test_get_node_val(self):
        self.assertEqual(1, self.node.get_node_val())


class TestBinaryTree(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBinaryTree, self).__init__(*args, **kwargs)
        self.binary_tree = BinaryTree([1, 2, 3, "null", 4, 5, "null"])

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class...")

    def setUp(self) -> None:
        print("set up")

    def tearDown(self) -> None:
        print("tear down")

    def test_BinaryTree(self):
        self.assertIsNotNone(self.binary_tree)

    def test_pre_order_traverse(self):
        self.assertEqual([1, 2, 4, 3, 5], self.binary_tree.pre_order_traverse())

    def test_in_order_traverse(self):
        self.assertEqual([2, 4, 1, 5, 3], self.binary_tree.in_order_traverse())

    def test_after_order_traverse(self):
        self.assertEqual([4, 2, 5, 3, 1], self.binary_tree.after_order_traverse())

    def test_build_binary_tree_from_an_incomplete_val_sequence(self):
        self.assertIsNotNone(self.binary_tree.build_binary_tree_from_an_incomplete_val_sequence([1, "null", 2, 3]))
