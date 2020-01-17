# -*- coding: utf-8 -*-

"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        Check whether can finish the course according to the prerequisites.

        Args:
            numCourses: int, number of courses to take.
            prerequisites: list(list(int)), the sequence of taking courses

        Returns:
            bool, whether can finish all the courses or not.

        """
        if len(prerequisites) < 2:
            return True
        # Store courses which input degree are zero
        queue = []
        requisity_dict = collections.defaultdict(list)
        for i in range(numCourses):
            requisity_dict[i] = []
        for pair in prerequisites:
            requisity_dict[pair[0]].append(pair[1])
        for k, v in requisity_dict.items():
            if len(v) == 0:
                queue.append(k)
        while queue:
            head = queue.pop(0)
            for k, v in requisity_dict.items():
                if head in v:
                    requisity_dict[k].remove(head)
                    if len(requisity_dict[k]) == 0:
                        queue.append(k)
        for k, v in requisity_dict.items():
            if len(v) > 0:
                return False
        return True





