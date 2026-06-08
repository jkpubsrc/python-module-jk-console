#!/usr/bin/python3



# see: https://stackoverflow.com/questions/5966903/how-to-get-mousemove-and-mouseclick-in-bash/55437976#55437976




import jk_console



print(jk_console.Console.MOUSE_ENABLE)



lastMouse = None

while True:

	x = jk_console.Console.Input.readKey()

	hexStr = ""
	for c in x:
		hexStr += "\\x" + format(ord(c), "x")

	if x.startswith(jk_console.Console.Input.MOUSE_EVENT):
		if lastMouse != x:
			lastMouse = x
			print(jk_console.Console.ForeGround.YELLOW + "mouse:\t" + repr(x) + "\t" + hexStr + jk_console.Console.RESET, flush=True)
	else:
		print("key:\t:" + repr(x) + "\t" + hexStr, flush=True)

	if x == "\x03":
		break



print(jk_console.Console.MOUSE_DISABLE)









