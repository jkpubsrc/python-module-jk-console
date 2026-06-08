#!/usr/bin/env python3

#
# This example demonstrates processing of mouse and keyboard events.
#



from jk_console import EventCollector, Console






class EventHandler(object):

	def on_mouse_wheel(self, ctx, bDown):
		if bDown:
			print(">>> Mouse wheel downward")
		else:
			print(">>> Mouse wheel upward")
	#

	def on_mouse_drag(self, ctx, nButton, x, y, buttonStates):
		print(">>> Mouse dragged at ({0}, {1}) with {2}".format(x, y, nButton))
	#

	def on_mouse_button(self, ctx, nButton, bPressed, x, y, buttonStates):
		if bPressed:
			print(">>> Mouse pressed at ({0}, {1}) with {2}".format(x, y, nButton))
		else:
			print(">>> Mouse released at ({0}, {1}) with {2}".format(x, y, nButton))
	#

	def on_screen_resized(self, ctx, oldW, oldH, w, h):
		print(">>> Console resized from ({0}, {1}) to ({2}, {3})".format(oldW, oldH, w, h))
	#

	def on_key_pressed(self, ctx, key):
		hexStr = ""
		for c in key:
			hexStr += "\\x" + format(ord(c), "x")
		print(">>> Key pressed:\t" + Console.Input.ALL_KEYS_TO_KEY_NAME.get(key, repr(key)) + "\t\t" + hexStr + "\t\t" + repr(key))
	#

	def on_ctrl_c(self, ctx, key):
		hexStr = ""
		for c in key:
			hexStr += "\\x" + format(ord(c), "x")
		print(">>> Ctrl+C pressed:\t" + Console.Input.ALL_KEYS_TO_KEY_NAME.get(key, repr(key)) + "\t\t" + hexStr + "\t\t" + repr(key))
		ctx.terminate()	
	#

#






EventCollector(
	EventHandler()
).run()









