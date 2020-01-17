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
        Using Topological sort, the process is as follows:
            1. build graph using dict(k:list)

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

    def canFinish2(self, numCourses, prerequisities):
        """
        Using DFS method to solve this problem.
        The key is that if visit a node which has been visited before means that there is a loop in the dfs process.
        In this case, return False. Otherwise return True.

        Args:
            numCourses: int, number of courses.
            prerequisities: list(list((int, int))), the dependencies of courses.

        Returns:
            bool, whether can finish the course schedule according to the prerequisities.
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for pair in prerequisities:
            graph[pair[1]].append(pair[0])
        for i in range(len(graph)):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph_list, visited_list, course_num):
        if visited_list[course_num]:
            return False
        else:
            visited_list[course_num] = 1
        for new_course_num in graph_list[course_num]:
            if not self.dfs(graph_list, visited_list, new_course_num):
                return False
        visited_list[course_num] = 0
        return True



