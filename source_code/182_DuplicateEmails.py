#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlez'

'''
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.
'''

class Solution(object):
	def getSQLStatement(self):
		"""
		rtype: str
		"""
		sql_statement = 'Select Email from Person group by Email having count(Email) > 1;'
		return sql_statement

# Another method using template
class Solution(object):
	def getSQLStatement(self):
		"""
		rtype: str
		"""
		sql_statement = "SELECT Email FROM (SELECT Email, count(Email) AS num FROM Person GROUP BY Email) AS Temtable WHERE num>1;"
		return sql_statement


