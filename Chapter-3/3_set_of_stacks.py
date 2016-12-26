# Set of Stacks

class Stack(object):

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.items:
			raise IndexError("Stack in empty")
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)

	def is_empty(self):
		return not bool(self.items)


class SetOfStack(object):

	def __init__(self, capacity):
		self.capacity = capacity
		self.stacks = []

	def push(self, item):
		if not self.stacks or self.stacks[i].size == self.capacity:
			new_stack = Stack()
			new_stack.push(item)
			self.stacks.push(new_stack)
		else:
			top_stack = self.stacks[-1]
			top_stack.push(item)

	def pop(self):
		if not self.stacks:
			raise IndexError("Stack is empty.")
		top_stack = self.stacks[-1]
		poped_item = top_stack.pop()
		if top_stack.size() == 0:
			self.stacks.pop()
