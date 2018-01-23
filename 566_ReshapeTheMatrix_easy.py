#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''

class Solution:
	def matrixReshape(self, nums, r, c):
		"""
		:type nums: List[List[int]]
		:type r: int
		:type c: int
		:rtype: List[List[int]]
		"""
		origin_r = len(nums)
		origin_c = len(nums[0])
		if origin_r * origin_c != r * c:
			return nums
		elements = []
		# typical wrong way: result = r*[c*[0]]
		result = [[0]*c for _ in range(r)]
		for i in range(origin_r):
			for j in range(origin_c):
				elements.append(nums[i][j])
		k = 0
		result[0][0] = 10000
		for i in range(r):
			for j in range(c):
				result[i][j] = elements[k]
				# print('result[%d][%d]:%d' % (i,j,result[i][j])) 
				# print(result)
				k = k + 1
				# print('k:', k)
		#print(result)
		return result

# test
# s = Solution()
# s.matrixReshape([[1,2],[3,4]], 4, 1)

# a = [[1,2],[3,4]]
# print(sum(a, []))
# print(map(list, zip(*([iter(sum(a, []))]*4))))
print(zip(([iter([1,2,3,4])] * 4)))


'''
Better Solution
'''

# first method: use Numpy
# import numpy as np
class Solution:
	def matrixReshape(self, nums, r, c):
		try:
			return np.reshape(nums, (r, c)).tolist()
		except:
			return nums


# second method: one line using zip and map
class Solution:
	def matrixReshape(self, nums, r, c):
		return nums if len(sum(nums, []))!=r*c else map(list, zip(*([iter(sum(nums, []))]*c))) 

# => a more readable version of method two

class Solution:
	def matrixReshape(self, nums, r, c):
		flat = sum(nums, [])
		if len(flat) != r*c:
			return nums
		tuples = zip(*([iter(flat)] * c))
		return map(list, tuples)

# itertools

class Solution:
	def matrixReshape(self, nums, r, c):
		if r * c != len(nums) * len(nums[0]):
			return nums
		it = itertools.chain(*nums)
		return [list(itertools.islice(it, c)) for _ in xrange(r)]

'''
range xrange:

1. range creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.

xrange is a generator, so it is a sequence object is a that evaluates lazily.

This is true, but in Python 3, range will be implemented by the Python 2 xrange(). If you need to actually generate the list, you will need to do:

list(range(1,100))

2. Remember, use the timeit module to test which of small snipps of code is faster!

$ python -m timeit 'for i in range(1000000):' ' pass'
10 loops, best of 3: 90.5 msec per loop
$ python -m timeit 'for i in xrange(1000000):' ' pass'
10 loops, best of 3: 51.1 msec per loop
Personally, I always use range(), unless I were dealing with really huge lists -- as you can see, time-wise, for a list of a million entries, the extra overhead is only 0.04 seconds. And as Corey points out, in Python 3.0 xrange will go away and range will give you nice iterator behaviour anyway.


'''

