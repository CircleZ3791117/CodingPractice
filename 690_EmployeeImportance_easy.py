# !/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Description:
You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Note:
One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.
'''

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

# recursive way
class Solution(object):
	def getImportance(self, employees, id):
		"""
		:type employees: Employee
		:type id: int
		:rtype: int
		"""
		im = 0
		def get_importance_recursively(employee, im, employees):
			im += employee.importance
			for subordinate in employee.subordinates:
				for employee in employees:
					if employee.id == subordinate:
						sub_employee = employee
						im = get_importance_recursively(sub_employee, im, employees)
						break
			return im
		for employee in employees:
			if employee.id == id:
				return get_importance_recursively(employee, im, employees)


# iterative
class Solution(object):
	def getImportance(self, employees, id):
		stack = []
		for employee in employees:
			if employee.id == id:
				target = employee
				stack = [target]
				break
		total_importance = 0
		while stack:
			head = stack.pop(0)
			total_importance += head.importance
			for subordinate_id in head.subordinates:
				for employee in employees:
					if employee.id == subordinate_id:
						stack.append(employee)
						break
		return total_importance


'''
Better Solution: using hash map
'''
class Solution(object):
	def getImportance(self, employees, id):
		e_map = {employee.id:employee for employee in employees}

		def dfs(id):
			return e_map[id].importance + sum(dfs(sub_id) for sub_id in e_map[id].subordinates)

		return dfs(id)


