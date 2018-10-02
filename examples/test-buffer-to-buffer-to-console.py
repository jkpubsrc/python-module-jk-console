#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


from jk_console import *

from FloatField import FloatField




def rangef(start, end, step):
	v = start
	while v <= end:
		yield v
		v += step
#



def createBackground(width, height, flavour:int):
	hueField = FloatField(width, height).fillRandom().smooth(8)
	luminanceField = FloatField(width, height).fillRandom().smooth(3)

	if flavour == 1:
		hueField.add(1 - hueField.maximum)
	elif flavour == 2:
		hueField.subtract((1 - hueField.minimum) / 1.5)

	rows = []
	for y in range(0, height):
		row = []
		for x in range(0, width):
			c = Console.BackGround.hsl1(
				hueField.data[y][x],
				1,
				luminanceField.data[y][x]
			)
			row.append(c)
		rows.append(row)
	return rows
#

def fillBufferWithBackground(backgroundData, buffer):
	for y in range(0, buffer.height):
		for x in range(0, buffer.width):
			buffer.set(x, y, backgroundData[y][x], " ")
#





Console.clear()
consoleWidth, consoleHeight = Console.getSize()
consoleBuffer = ConsoleBuffer(consoleWidth - 4, consoleHeight - 4)

fillBufferWithBackground(
	createBackground(consoleBuffer.width, consoleBuffer.height, 0),
	consoleBuffer)
consoleBuffer.bufferToConsole(2, 2)

extraBuffer1 = ConsoleBuffer(int(consoleBuffer.width / 1.5), int(consoleBuffer.height / 1.5))
fillBufferWithBackground(
	createBackground(extraBuffer1.width, extraBuffer1.height, 1),
	extraBuffer1)
extraBuffer1.bufferToBuffer(6, 3, consoleBuffer)
consoleBuffer.bufferToConsole(2, 2)

extraBuffer2 = ConsoleBuffer(int(consoleBuffer.width / 1.5), int(consoleBuffer.height / 1.5))
fillBufferWithBackground(
	createBackground(extraBuffer2.width, extraBuffer2.height, 2),
	extraBuffer2)
extraBuffer2.bufferToBuffer(consoleBuffer.width - extraBuffer2.width + 6, consoleBuffer.height - extraBuffer2.height + 3, consoleBuffer)
consoleBuffer.bufferToConsole(2, 2)

















