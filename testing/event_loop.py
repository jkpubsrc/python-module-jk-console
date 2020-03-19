#!/usr/bin/python3



import jk_console



print(jk_console.Console.MOUSE_ENABLE)

for evt, evtData, keyName in jk_console.Console.Input.produceEventsLoop():
	if evt == "key":
		if evtData == "\x03":
			print(jk_console.Console.MOUSE_DISABLE)
			break
		if len(evtData) == 1:
			print(evt, hex(ord(evtData)), repr(evtData))
		else:
			if keyName:
				print(evt, keyName)
			else:
				print(evt, [ hex(ord(x)) for x in evtData ])
	else:
		print(evt, evtData)
