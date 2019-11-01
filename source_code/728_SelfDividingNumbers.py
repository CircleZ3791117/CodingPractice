#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
'''

'''
Solution:
for integer in range(left, right+1), judge the numbers in it
'''
class Solution:
	def selfDividingNumbers(self, left, right):
		"""
		:type left: int
		:type right: int
		:rtype: List[int]
		"""
		results = []
		for number in range(left, right+1):
			number_str = str(number)
			flag = True
			for digit in number_str:
				if digit == '0':
					flag = False
					break
				elif number % int(digit) != 0:
					flag = False
					break
			if flag == True:
				results.append(number)
		return results

'''
Better Solution: use lambda and all()
'''
class Solution:
	def selfDividingNumbers(self, left, right):
		isDividingNumber = lambda x: '0' not in str(x) and all(x%int(i) == 0 for i in str(x))
		return filter(isDividingNumber, range(left, right+1))

'''
python all() and any():

You can roughly think of any and all as series of logical or and and operators, respectively.

any

any will return True when at least one of the elements is Truthy. Read about Truth Value Testing.

all

all will return True only when all the elements are Truthy.

Truth table

+-----------------------------------------+---------+---------+
|                                         |   any   |   all   |
+-----------------------------------------+---------+---------+
| All Truthy values                       |  True   |  True   |
+-----------------------------------------+---------+---------+
| All Falsy values                        |  False  |  False  |
+-----------------------------------------+---------+---------+
| One Truthy value (all others are Falsy) |  True   |  False  |
+-----------------------------------------+---------+---------+
| One Falsy value (all others are Truthy) |  True   |  False  |
+-----------------------------------------+---------+---------+
| Empty Iterable                          |  False  |  True   |
+-----------------------------------------+---------+---------+
Note 1: The empty iterable case is explained in the official documentation, like this

any

Return True if any element of the iterable is true. If the iterable is empty, return False

Since none of the elements is true, it returns False in this case.

all

Return True if all elements of the iterable are true (or if the iterable is empty).

Since none of the elements is false, it returns True in this case.

Note 2:

Another important thing to know about any and all is, it will short-circuit the execution, the moment they know the result. The advantage is, entire iterable need not be consumed. For example,

>>> multiples_of_6 = (not (i % 6) for i in range(1, 10))
>>> any(multiples_of_6)
True
>>> list(multiples_of_6)
[False, False, False]
Here, (not (i % 6) for i in range(1, 10)) is a generator expression which returns True if the current number within 1 and 9 is a multiple of 6. any iterates the multiples_of_6 and when it meets 6, it finds a Truthy value, so it immediately returns True, and rest of the multiples_of_6 is not iterated. That is what we see when we print list(multiples_of_6), the result of 7, 8 and 9.

This excellent thing is used very cleverly in this answer.

With this basic understanding, if we look at your code, you do

any(x) and not all(x)
which makes sure that, atleast one of the values is Truthy but not all of them. That is why it is returning [False, False, False]. If you really wanted to check if both the numbers are not the same,

print [x[0] != x[1] for x in zip(*d['Drd2'])]
'''