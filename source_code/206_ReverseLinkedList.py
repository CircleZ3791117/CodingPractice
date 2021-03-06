#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		value_list = []
		p = head
		while p:
			value_list.append(p.val)
			p = p.next
		reverse_value = value_list[::-1]
		p = head
		print(reverse_value)
		for i in range(len(value_list)):
			p.val = reverse_value[i]
			p = p.next
		return head


# Using iterative method
class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head:
			return
		tail = head
		while tail.next:
			tail = tail.next
		first = head
		second = first.next
		while second:
			if second.next:
				tmp = second.next
			else:
				second.next = first
				break
			second.next = first
			first = second
			second = tmp
		head.next = None
		return tail

# Using recursive method
class Solution(object):
	def reverseList(self, head):
		if not head or not head.next:
			return head
		p = self.reverseList(head.next)
		head.next.next = head
		head.next = None
		return p


