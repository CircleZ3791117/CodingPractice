# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Example 1:
Input: ["5","2","C","D","+"]
Output: 30
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.  
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
Example 2:
Input: ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.  
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.
Note:
The size of the input list will be between 1 and 1000.
Every integer represented in the list will be between -30000 and 30000.
'''

'''
Solution
'''
import re
class Solution:
	def calPoints(self, ops):
		"""
		:type ops: List[str]
		:rtype: int
		"""
		sum = 0
		score = [0]*len(ops)
		valid_round = [0]*len(ops)
		for i in range(len(ops)):
			if re.match('[-1-9]+',ops[i]):
				score[i] = int(ops[i])
				valid_round[i] = 1
				# print(i, ops[i], ':', score[i])
			elif ops[i] == 'C':
				j = i-1
				while(j>=0):
					if score[j] != None:
						score[j] = None
						score[i] = None
						valid_round[j] = 0
						break
					j = j - 1
				valid_round[i] = 0
				# print(i, ops[i], ':', score[i])
			elif ops[i] == 'D':
				j = i - 1
				while(j >= 0):
					if valid_round[j] == 1:
						score[i] = score[j] * 2
						valid_round[i] = 1
						break
					j = j - 1
				valid_round[i] = 1
				# print(i, ops[i], ':', score[i])
			elif ops[i] == '+':
				j = i - 1
				count = 0
				while(j >=0 and count < 2):
					if valid_round[j] == 1:
						score[i] += score[j]
						count += 1
					j = j - 1
				valid_round[i] = 1
				# print(i, ops[i], ':', score[i])
			else:
				raise ValueError('Invalid input!')
		for item in score:
			if item != None:
				sum += item
		return sum

# test:
# s = Solution()
# s.calPoints(["-60","D","-36","30","13","C","C","-33","53","79"])

'''
How to initialize list with length n:

If the "default value" you want is immutable, e.g. [0]*10, is good enough.

But if you want, say, a list of ten dicts, do not use [{}]*10 -- that would give you a list with the same initially-empty dict ten times, not ten distinct ones. Rather, use [{} for i in range(10)] or similar constructs, to construct ten separate dicts to make up your list.
'''

'''
Better Solution
Key: use stack
'''
import re
class Solution:
	def calPoints(self, ops):
		"""
		:ops type: List[str]
		:rtype: int
		"""
		history = []	# use history as a stack
		for op in ops:
			if op == 'C':
				history.pop()
			elif op == 'D':
				history.append(history[-1]*2)
			elif op == '+':
				history.append(history[-1] + history[-2])
			elif re.match('[-1-9]+', op):
				history.append(int(op))
			else:
				raise ValueError('Invalid op!')
		return sum(history)

