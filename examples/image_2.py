#!/usr/bin/env python3

#
# This example demonstrates color output.
# In this case RGB colors are generated. Please note that this might not work
# on older systems if RGB is not supported.
#



import os
import sys
from PIL import Image

from jk_console import *





Console.clear()
consoleWidth, consoleHeight = Console.getSize()
consoleBuffer = ConsoleBufferRGB2(consoleWidth, consoleHeight, bgColor=IntRGB.parseCSS("#000000"))
charBuffer = ConsoleBufferRGB2(consoleWidth - 2, consoleHeight - 3)


for fileName in os.listdir("images"):
	if not fileName.endswith(".jpg"):
		continue

	consoleBuffer.fill(IntRGB.parseCSS("#000000"), None)
	consoleBuffer.bufferToConsole()

	charBuffer.fill(IntRGB.parseCSS("#000000"), None)
	image = Image.open("images/" + fileName, "r")
	image = image.resize((image.width * 2, image.height))
	image.thumbnail((charBuffer.width, charBuffer.height))
	pixelValues = list(image.getdata())
	for y in range(0, image.height):
		for x in range(0, image.width):
			v = pixelValues[x + y*image.width]
			charBuffer.set(x, y, IntRGB.rgb256(v[0], v[1], v[2]), None, " ")
	posX = (consoleWidth - image.width) // 2
	posY = (consoleHeight - image.height) // 2 + 1
	charBuffer.bufferToBufferCopy(posX, posY, consoleBuffer)

	consoleBuffer.printText(0, 0, IntRGB.BLACK, IntRGB.WHITE, fileName)
	consoleBuffer.bufferToConsole()
	Console.moveCursorTo(len(fileName) + 1, 0)

	if Console.Input.readKey() == Console.Input.KEY_CTRL_C:
		break

Console.clear()







