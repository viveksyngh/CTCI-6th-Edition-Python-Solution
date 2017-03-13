# Write a program to sort stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (Such as an array). The stack supports the following
# operations: push, pop, peek and isEmpty

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

	def size(self):
		return len(self.items)


def sort_stack(stack):
	temp_stack = Stack() # Temporary stack
	n = stack.size()
	i = n
	while i > 0:
		max_value = -1

		# Swapping all remanining elements from original stack to temp stack
		while not stack.is_empty():
			poped_item = stack.pop()
			max_value = max(max_value, poped_item) # Getting max value for this swap
			temp_stack.push(poped_item)
		
		# Swapping back all elements lesser than current max value
		for j in range(i):
			temp_poped = temp_stack.pop()
			if temp_poped != max_value:
				stack.push(temp_poped)
		temp_stack.push(max_value)
		
		i -= 1
	return temp_stack


if __name__ == '__main__':
	s1 = Stack()
	s1.push(1)
	s1.push(5)
	s1.push(3)
	s1.push(2)
	s1.push(4)
	s1.push(6)
	print sort_stack(s1).items


