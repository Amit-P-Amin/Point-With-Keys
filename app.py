import pythoncom, pyHook

class KeyboardHandler:

	def __init__(self):
		self.shouldRun = True 
		self.store     = []

	def lastKey(self):
		if len(self.store) == 0:
			return ''
		else:
			return self.store[-1]

	def OnKeyboardEvent(self, event):
		print('Ascii:', event.Ascii, chr(event.Ascii))
		print(self.lastKey())

		if chr(event.Ascii) == 'e' and self.lastKey() != 'e':
			self.store.append('e')
			return False

		if chr(event.Ascii) == 'e' and self.lastKey() == 'e':
			self.store.pop()
			self.shouldRun = False 
			return False	

		return True

	def start(self):
		hookManager         = pyHook.HookManager()
		hookManager.KeyDown = self.OnKeyboardEvent
		hookManager.HookKeyboard()

		while self.shouldRun:
			pythoncom.PumpWaitingMessages()

KeyboardHandler().start()
