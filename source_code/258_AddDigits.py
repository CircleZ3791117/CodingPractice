#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

'''
Solution
'''
# recursively
class Solution:
	def addDigits(self, num):
		def add_recursively(number):
			if 0 <= number <= 9:
				return number
			number = sum([int(i) for i in str(number)])
			return add_recursively(number)
		return add_recursively(num)



# test
s = Solution()
s.addDigits(10)

# iteration
class Solution:
	def addDigits(self, num):
		while(num > 9):
			s = 0
			while(num > 0):
				s += num % 10
				num  /= 10
			num = s
		return num
'''
Better Solution:
this method depends on the truth:

N=(a[0] * 1 + a[1] * 10 + …a[n] * 10 ^n),and a[0]…a[n] are all between [0,9]

we set M = a[0] + a[1] + …a[n]

and another truth is that:

1 % 9 = 1

10 % 9 = 1

100 % 9 = 1

so N % 9 = a[0] + a[1] + …a[n]

means N % 9 = M

so N = M (% 9)

as 9 % 9 = 0,so we can make (n - 1) % 9 + 1 to help us solve the problem when n is 9.as N is 9, ( 9 - 1) % 9 + 1 = 9
'''
class Solution:
	def addDigits(self, num):
		return num % 9 or 9 if num else 0
