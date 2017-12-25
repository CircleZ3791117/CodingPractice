# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''

'''
Solution
'''
print((2%3 and 2%5) * str(2))
class Solution:
	def fizzBuzz(self, n):
		results = []
		for i in range(1, n+1):
			if i%3 == 0 and i%5 == 0:
				results.append('FizzBuzz')
			elif i%3 == 0:
				results.append('Fizz')
			elif i%5 == 0:
				results.append('Buzz')
			else:
				results.append(str(i))
		return results


"""
Better Solution
"""
class Solution:
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		return ['Fizz'*(not i % 3) + 'Buzz'*(not i % 5) or str(i) for i in range(1, n+1)]

