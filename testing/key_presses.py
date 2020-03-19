#!/usr/bin/python3


import jk_utils
import jk_console


while True:
	k = jk_console.Console.Input.readKey()
	if (k is None) or (k == jk_console.Console.Input.KEY_CTRL_BREAK):
		break
	keyText = jk_console.Console.Input.ALL_KEYS_TO_KEY_NAME.get(k, k)
	
	hexText = "".join([ jk_utils.hex.byteToHex(ord(kk)) for kk in k ])
	print(hexText + "\t" + keyText)












