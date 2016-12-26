# Implement a MyQueue class which implements a queue using two stacks


class Stack(object):

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.items:
			raise IndexError("Stack is empty.")
		return self.items.pop()

	def is_empty(self):
		return not bool(self.items)

	def peek(self):
		return self.items[-1]


class MyQueue(object):

	def __init__(self):
		self.newestStack = Stack()
		self.oldestStack = Stack()

	def size(self):
		return self.oldestStack.size() + self.newestStack.size()

	def add(self, item):
		self.newestStack.push(item)

	def move_items(self):
		if self.oldestStack.is_empty():
			while not self.newestStack.is_empty():
				self.oldestStack.push(self.newestStack.pop())

	def remove(self):
		self.move_items()
		return self.oldestStack.pop()

	def peek(self):
		self.move_items()
		return self.oldestStack.peek()
	


