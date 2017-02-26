class Store:

	def __init__(self):
		self.keyPresses = []

	def lastPress(self):
		if len(self.keyPresses) == 0:
			return ''
		else:
			return self.keyPresses[-1]

	def add(self, char):
		self.keyPresses.append(char)

	def clear(self):
		self.keyPresses = []