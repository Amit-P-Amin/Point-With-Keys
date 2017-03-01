class State:

	def __init__(self):
		self.currentState  = "STARTING"
		self.pointerAction = None

	def enterMouseMode(self, pointerAction):
		self.currentState  = "VERTICAL_POSITIONING"
		self.pointerAction = pointerAction

	def isStarting(self):
		return self.currentState == "STARTING"

	def isPositioning(self):
		return self.currentState == "VERTICAL_POSITIONING" or self.currentState == "HORIZONTAL_POSITIONING" 

	def clear(self):
		self.currentState  = "STARTING"
		self.pointerAction = None