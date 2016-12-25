# How would you design a stack which, in addition to push and pop,
# has a function min which returns the minimum element? Push, pop
# and min should all operate in O(1) time.


# Solution one : - Which stores minimum value with each node of stack
class MinStackNode(object):

	def __init__(self, value, min):
		self.value = value
		self.min = min


class MinStack(object):

	def __init__(self):
		self.items = []

	def push(self, item):
		new_min = min(self.min(), item)
		node = MinStackNode(item, new_min)
		self.items.append(node)

	def pop(self):
		if self.items:
			item = self.items.pop()
			return item.value
		else:
			raise IndexError("Stack is empty.")

	def min(self):
		if not self.items:
			return 2 ** 31 - 1
		return self.items[-1].min

	def peek(self):
		if not self.items:
			raise IndexError("Stack in empty.")
		return self.items[-1].value

	def is_empty(self):
		return not bool(self.items)

# Solution two :-  Uses two stack one for items and other for min value

class Stack(object):

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.items:
			raise IndexError("Stack is empty.")
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def is_empty(self):
		return not bool(self.items)


class MinStack2(object):

	def __init__(self):
		self.stack = Stack()
		self.items = []

	def push(self, item):
		if self.stack.is_empty():
			self.stack.push(item)
		else : 
			if self.stack.peek() > item:
				self.stack.push(item)
		self.items.push(item)

	def pop(self, item):
		if not self.items:
			raise IndexError("Stack in empty")
		if self.items[-1] == self.stack.peek():
			self.stack.pop()
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def is_empty(self):
		return not bool(self.items)
	



