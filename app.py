import pythoncom, pyHook

class KeyHandler:

	def __init__(self):
		self.run = True 

	def OnKeyboardEvent(self, event):
		print('Ascii:', event.Ascii, chr(event.Ascii))
		self.run = False
		return False	

	def start(self):
		# create a hook manager
		hookManager = pyHook.HookManager()
		# watch for all mouse events
		hookManager.KeyDown = self.OnKeyboardEvent
		# set the hook
		hookManager.HookKeyboard()
		while self.run:
			pythoncom.PumpWaitingMessages()

x = KeyHandler()
print(x)
x.start()
