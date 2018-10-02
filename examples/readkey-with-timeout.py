#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from jk_console import Console






print()
print("key name\thex\t\tstr()")
print()

while True:
	key = Console.Input.readKeyWithTimeout(1)
	if key is None:
		print("(no-key)")
		continue

	hexStr = ""
	for c in key:
		hexStr += "\\x" + format(ord(c), "x")
	print(Console.Input.ALL_KEYS_TO_KEY_NAME.get(key, repr(key)) + "\t\t" + hexStr + "\t\t" + repr(key))
	if key is Console.Input.KEY_CTRL_C:
		break

print()












