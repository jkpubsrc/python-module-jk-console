#!/usr/bin/env python3



import sys
import time

import jk_console



#osb = jk_console.CharacterBuffer(100, 20, bgColor = jk_console.Console.BackGround.STD_DARKYELLOW)
#osb.clear()

jk_console.Console.clear()
w, h = jk_console.Console.getSize()
cb = jk_console.ConsoleBuffer(width = w - 6, height = h - 6)
cb.bufferToConsole(ofsX = 3, ofsY = 3)

"""
cb.fill(10, 5, 50, 5, jk_console.Console.BackGround.STD_BLUE + jk_console.Console.ForeGround.STD_YELLOW, "/")
osb.copyToConsoleBuffer0(13, 8, cb)
cb.fill(20, 15, 50, 5, jk_console.Console.BackGround.STD_BLUE + jk_console.Console.ForeGround.STD_YELLOW, "\\")
cb.bufferToConsole()
"""

m = max(cb.width, cb.height)
for i in range(cb.width - 1, -1, -1):
	x = i % cb.width
	y = i % cb.height
	c = jk_console.Console.ForeGround.STD_CYAN + jk_console.Console.BackGround.STD_BLUE
	c = jk_console.Console.ForeGround.STD_CYAN + jk_console.Console.BackGround.hsl1(i / cb.width, 1, 0.5)
	for xj in range(0, x):
		cb.set(xj, y, c, str(i)[-1])
	c = jk_console.Console.RESET
	if x < cb.width - 1:
		cb.set(x + 1, y, c, " ")
	if x < cb.width - 2:
		cb.set(x + 2, y, c, " ")
	c = jk_console.Console.ForeGround.STD_BLACK + jk_console.Console.BackGround.STD_LIGHTGRAY
	cb.set(x, y, c, str(i)[-1])
cb.bufferToConsole(ofsX = 3, ofsY = 3)



"""
m = max(cb.width, cb.height)
for i in range(0, 70):
	x = i % cb.width
	y = i % cb.height
	jk_console.Console.printAt(x, y, jk_console.Console.BackGround.STD_DARKYELLOW + jk_console.Console.ForeGround.STD_CYAN + str(i)[-1] + jk_console.Console.RESET, True)
"""





