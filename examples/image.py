#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
from PIL import Image

from jk_console import *





Console.clear()
consoleWidth, consoleHeight = Console.getSize()
consoleBuffer = ConsoleBuffer(consoleWidth, consoleHeight)
charBuffer = ConsoleBuffer(consoleWidth - 2, consoleHeight - 3)


for fileName in os.listdir("images"):
	if not fileName.endswith(".jpg"):
		continue

	consoleBuffer.clear()
	consoleBuffer.printText(0, 0, Console.ForeGround.WHITE, fileName)

	charBuffer.clear()
	image = Image.open("images/" + fileName, "r")
	image = image.resize((image.width * 2, image.height))
	image.thumbnail((charBuffer.width, charBuffer.height))
	pixelValues = list(image.getdata())
	for y in range(0, image.height):
		for x in range(0, image.width):
			v = pixelValues[x + y*image.width]
			charBuffer.set(x, y, Console.BackGround.rgb256(v[0], v[1], v[2]), " ")
	posX = (consoleWidth - image.width) // 2
	posY = (consoleHeight - image.height) // 2 + 1
	charBuffer.bufferToBuffer(posX, posY, consoleBuffer)

	consoleBuffer.bufferToConsole(bForceFullRepaint=True)
	Console.moveCursorTo(len(fileName) + 1, 0)

	if Console.Input.readKey() == Console.Input.KEY_CTRL_C:
		break

Console.clear()







