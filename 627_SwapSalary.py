# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a table salary, such as the one below, that has m=male and f=female values. Swap all f and m values (i.e., change all f values to m and vice versa) with a single update query and no intermediate temp table.
For example:
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
After running your query, the above salary table should have the following rows:
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
'''

'''
Solution:
UPDATE table SET column = ... 
CASE [WHEN ... THEN ...] ELSE ... END
caution: equal -> = not ==
'''

def getSQLStatement():
	sql_str = "UPDATE salary SET sex=(CASE WHEN (sex='m') THEN 'f' WHEN (sex='f') THEN 'm' ELSE sex END)"
	# wrong: sql_str = "UPDATE salary SET sex=(CASE WHEN (sex=='m') THEN 'f' WHEN (sex=='f') THEN 'm' ELSE sex END)"
	return sql_str

'''
Better Solution
'''
# 1. CASE [WHEN ... THEN ...] ELSE ... END 
# This method is faster than the other two methods
def get getSQLStatement():
	sql_str = "UPDATE salary SET sex= CASE WHEN sex='m' THEN 'f' ELSE 'm' END"
	return sql_str

# 2. IF(condion, y, n)
def get getSQLStatement():
	sql_str = "UPDATE salary SET sex= IF(sex='m', 'f', 'm')"
	return sql_str

# 3. use XOR to exchange two value
# you can use XOR to exchange two values in nearly all cases
# For example:
# a = 1, b = 0 . You can switch value like this:
# b = a ^ b => b = 1
# a = a ^ b => a = 0
def get getSQLStatement():
	sql_str = "UPDATE salary SET sex= CHAR(ASCII('m') ^ ASCII('f') ^ ASCII(sex))"
	return sql_str