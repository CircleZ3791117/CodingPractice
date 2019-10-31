#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

 

Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
 

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.
'''

class Foo:
	def __init__(self):
		pass

	def first(self, printFirst: 'Callable[[], None]') -> None:
		# printFirst() outputs "first". Do not change or remove this line.
		printFirst()

	def second(self, printSecond: 'Callable[[], None]') -> None:
		# printSecond() outputs "second". Do not change or remove this line.
		printSecond()

	def third(self, printThird: 'Callable[[], None]') -> None:
		# printThird() ouputs "third". Do not change or remove this line.
		printThird()

# Solution
# Basically, we can use five ways to solve this problem in python which are Barrier, Lock, Semaphore, Event and Condition. The solutions are as follows:

# Using Barrier
from threading import Barrier
class Foo:
	def __init__(self):
		self.first_barrier = Barrier(2)
		self.second_barrier = Barrier(2)

	def first(self, printFirst: 'Callable[[], None]') -> None:
		printFirst()
		self.first_barrier.wait()

	def second(self, printSecond: 'Callable[[], None]') -> None:
		self.first_barrier.wait()
		printSecond()
		self.second_barrier.wait()

	def third(self, printThird: 'Callable[[], None]') -> None:
		self.second_barrier.wait()
		printThird()

# Using Lock
from threading import Lock
class Foo:
	def __init__(self):
		self.locks = (Lock(), Lock())
		self.locks[0].acquire()
		self.locks[1].acquire()

	def first(self, printFirst: 'Callable[[], None]') -> None:
		printFirst()
		self.locks[0].release()

	def second(self, printSecond: 'Callable[[], None]') -> None:
		with self.locks[0]:
			printSecond()
			self.locks[1].release()

	def third(self, printThird: 'Callable[[], None]') -> None:
		with self.locks[1]:
			printThird()

# Using Event
from threading import Event

class Foo:
	def __init__(self):
		self.done = (Event(), Event())

	def first(self, printFirst: 'Callable[[], None]') -> None:
		printFirst()
		self.done[0].set()

	def second(self, printSecond: 'Callable[[], None]') -> None:
		self.done[0].wait()
		printSecond()
		self.done[1].set()

	def third(self, printThird: 'Callable[[], None]') -> None:
		self.done[1].wait()
		printThird()

# Using Semaphore
from threading import Semaphore

class Foo:
	def __init__(self):
		self.gates = (Semaphore(0), Semaphore(0))

	def first(self, printFirst: 'Callable[[], None]') -> None:
		printFirst()
		self.gates[0].release()

	def second(self, printSecond: 'Callable[[], None]') -> None:
		with self.gates[0]:
			printSecond()
			self.gates[1].release()

	def third(self, printThird: 'Callable[[], None]') -> None:
		with self.gates[1]:
			printThird()


# Using Condition
from threading import Condition
class Foo:
	def __init__(self):
		self.exec_condition = Condition()
		self.order = 0
		self.first_finish = lambda: self.order == 1
		self.second_finish = lambda: self.order == 2

	def first(self, printFirst: "Callable[[], None]") -> None:
		with self.exec_condition:
			printFirst()
			self.order = 1
			self.exec_condition.notify(2)

	def second(self, printSecond: "Callable[[], None]") -> None:
		with self.exec_condition:
			self.exec_condition.wait_for(self.first_finish)
			printSecond()
			self.order = 2
			self.exec_condition.notify()

	def third(self, printThird: "Callable[[], None]") -> None:
		with self.exec_condition:
			self.exec_condition.wait_for(self.second_finish)
			printThird()