from store import Store
from state import State
import pythoncom, pyHook
import win32api, win32con

KEY_E = 0x45

ip.ki.wVk = 0x41; // virtual-key code for the "a" key
ip.ki.dwFlags = 0; // 0 for key press
SendInput(1, &ip, sizeof(INPUT));

class KeyboardHandler:

	def __init__(self):
		self.shouldRun = True 
		self.store     = Store()
		self.state     = State()

	def OnKeyboardEvent(self, event):
		print('Ascii:', event.Ascii, chr(event.Ascii))
		lastPress  = self.store.lastPress()
		keyPressed = chr(event.Ascii)
		self.store.add(keyPressed)

		if self.state.isStarting():
			if chr(event.Ascii) == 'e' and lastPress != 'e':
				# Prepare to exit, capture 'e'
				return False	

			if chr(event.Ascii) != 'e' and lastPress == 'e':
				# Exit sequence aborted, release 'e'
				win32api.keybd_event(KEY_E,0,0,0)

			if chr(event.Ascii) == 'e' and lastPress == 'e':
				# Run 'ee' exit command
				self.store.clear()
				self.shouldRun = False 
				return False	

			if chr(event.Ascii) == 'a' and lastPress != 'a':
				# Prepare to enter left click mode, capture 'a'
				return False

			if chr(event.Ascii) != 'a' and lastPress == 'a':
				# Left click sequence aborted, release 'a'
				return False

			if chr(event.Ascii) == 'a' and lastPress == 'a':
				# Enter 'aa' left click mode
				self.store.clear()
				self.state.enterMouseMode('leftClick') 
				return False

		if self.state.isPositioning():			
			# Placeholder
			if chr(event.Ascii) == 'a':
				return False
				self.store.clear()
				self.state.clear()

		if event.Ascii == 27:
			# Reset if 'esc' key entered
			self.store.clear()
			self.state.clear()

		return True

	def start(self):
		hookManager         = pyHook.HookManager()
		hookManager.KeyDown = self.OnKeyboardEvent
		hookManager.HookKeyboard()

		while self.shouldRun:
			pythoncom.PumpWaitingMessages()

# KeyboardHandler().start()
