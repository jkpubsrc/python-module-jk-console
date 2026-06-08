#!/usr/bin/env python3

#
# This example demonstrates reading data from the keyboard without timeout.
#



from jk_console import Console




print()
print("key name\thex\t\tstr()")
print()

while True:
	key = Console.Input.readKey()
	hexStr = ""
	for c in key:
		hexStr += "\\x" + format(ord(c), "x")
	print(Console.Input.ALL_KEYS_TO_KEY_NAME.get(key, repr(key)) + "\t\t" + hexStr + "\t\t" + repr(key))
	if key is Console.Input.KEY_CTRL_C:
		break

print()







