# -*- coding: utf-8 -*-

"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.



Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.


Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
"""


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Return a deep copy of given node.

        Args:
            node: Node, start node of target undirected graph.

        Returns:
            Node, a deep copy reference of target node.

        """
        # # Set copied_list and new_node_list to avoid redundant copy
        # copied_list = []  # Node that has already been copied in the target graph.
        # new_node_list = []  # new created node
        # return self.deep_copy(node, copied_list, new_node_list)

        return self.deep_copy_using_bfs(node)

    def deep_copy(self, source_node, copied_list, new_node_list):
        """
        Deep copy method for undirected graph. (DFS)

        Args:
            source_node: Node, start point at the target graph.
            copied_list: list, already copied node list.
            new_node_list: list, new created node list.

        Returns:
            Node reference, deep copy of given node.
        """
        if not source_node:
            return
        new_node = Node(source_node.val, [])
        copied_list.append(source_node)  # already copied source node
        new_node_list.append(new_node)  # new node list
        for neighbor_node in source_node.neighbors:
            if neighbor_node in copied_list:
                # New created node and copied node have the same index.
                new_node.neighbors.append(new_node_list[copied_list.index(neighbor_node)])
            else:
                # Once the node has not been copied before, create a new tmp node recursively
                tmp_node = self.deep_copy(neighbor_node, copied_list, new_node_list)
                new_node.neighbors.append(tmp_node)
        return new_node

    def deep_copy_using_bfs(self, source_node):
        """
        Traverse all the node using breath first method.

        Args:
            source_node: Node, start point at the target graph.

        Returns:
            Node, return a deep copy node reference.
        """
        if not source_node:
            return
        queue = [source_node]  # first in first out
        node = Node(source_node.val, [])
        copied_node_list = [source_node]  # Already copied node in target graph.
        new_node_list = [node]  # New created node.

        while queue:
            head = queue.pop(0)
            new_node = new_node_list[copied_node_list.index(head)]
            for neighbor in head.neighbors:
                if neighbor not in copied_node_list:
                    tmp = Node(neighbor.val, [])  # Create new code.
                    new_node.neighbors.append(tmp)
                    copied_node_list.append(neighbor)
                    new_node_list.append(tmp)
                    queue.append(neighbor)  # Add copied node to queue.
                else:
                    new_node.neighbors.append(new_node_list[copied_node_list.index(neighbor)])
        return node
