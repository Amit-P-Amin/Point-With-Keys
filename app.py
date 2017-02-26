from store import Store
import pythoncom, pyHook
import win32api, win32con

KEY_E = 0x45

class KeyboardHandler:

	def __init__(self):
		self.shouldRun = True 
		self.store     = Store()

	def OnKeyboardEvent(self, event):
		print('Ascii:', event.Ascii, chr(event.Ascii))
		lastPress  = self.store.lastPress()
		keyPressed = chr(event.Ascii)
		self.store.add(keyPressed)

		if chr(event.Ascii) == 'e' and lastPress != 'e':
			# Prepare to exit, capture 'e'
			return False	

		if chr(event.Ascii) != 'e' and lastPress == 'e':
			# Abort exit, release 'e'
			win32api.keybd_event(KEY_E,0,0,0)

		if chr(event.Ascii) == 'e' and lastPress == 'e':
			# Accept and run 'ee' exit sequence
			self.store.clear()
			self.shouldRun = False 
			return False	


		# if chr(event.Ascii) == 'a' and self.store.lastPress() != 'a':
		# 	self.store.add('a')
		# 	return False

		# if chr(event.Ascii) == 'a' and self.store.lastPress() == 'a':
		# 	self.store.clear()
		# 	self.shouldRun = False 
		# 	return False

		return True

	def start(self):
		hookManager         = pyHook.HookManager()
		hookManager.KeyDown = self.OnKeyboardEvent
		hookManager.HookKeyboard()

		while self.shouldRun:
			pythoncom.PumpWaitingMessages()

KeyboardHandler().start()
