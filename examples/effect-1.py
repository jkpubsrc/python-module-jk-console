#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import time
import datetime

from jk_console import *



#osb = jk_console.CharacterBuffer(100, 20, bgColor = jk_console.Console.BackGround.STD_DARKYELLOW)
#osb.clear()


chars = ".,;/;,. "
colors = [ Console.ForeGround.STD_LIGHTGRAY, Console.ForeGround.STD_BLUE, Console.ForeGround.STD_LIGHTBLUE, Console.ForeGround.STD_LIGHTCYAN,
	Console.ForeGround.STD_LIGHTBLUE, Console.ForeGround.STD_BLUE, Console.ForeGround.STD_LIGHTGRAY, Console.RESET ]
w = None
h = None
cb = None
mods = [ 0, -1, -1, -2, -2, -1, -1, 0 ]

def init():
	global w, h, cb

	Console.clear()
	cb = ConsoleBuffer()
	cb.bufferToConsole()

	rect = Rect(0, 0, cb.width, cb.height)
	rect = rect.shrink(right = 1, bottom = 1)
	cb.drawFrame(rect = rect)

	w = cb.width
	h = cb.height
#

def drawPattern(cb:ConsoleBuffer, ofs:int):
	for iy in range(1, h - 2):
		for ix in range(2, w - 2):
			j = (iy + ofs) % 8
			i = (ix + iy + ofs + mods[j]) % 8
			cb.set(ix, iy, colors[i], chars[i])
#

init()

drawPattern(cb, 0)
i = 1
while True:
	time.sleep(0.05)

	t0 = datetime.datetime.now()
	drawPattern(cb, i)
	t1 = datetime.datetime.now()
	cb.bufferToConsole(bForceFullRepaint=True)
	t2 = datetime.datetime.now()

	time.sleep(0.001)

	td1 = t1 - t0
	td2 = t2 - t1
	tdS = t2 - t0
	pdata = ("~~ screen-size: ", str(w), "x", str(h), " pixels"
		" ~~ rendering: %d.%03ds" % (td1.seconds, (td1.microseconds + 499) // 1000),
		" ~~ buffer-to-screen: %d.%03ds" % (td2.seconds, (td2.microseconds + 499) // 1000),
		" ~~ total: %d.%03ds (fps %d)" % (tdS.seconds, (tdS.microseconds + 499) // 1000, int(1.0 / (t2 - t0).total_seconds())),
		" ~~",
	)
	cb.printText(2, h - 2, Console.ForeGround.STD_WHITE, "".join(pdata))
	i += 1

	ww = Console.width() - 1
	hh = Console.height() - 1
	if (ww != w) or (hh != h):
		init()

