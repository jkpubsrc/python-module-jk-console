#!/usr/bin/env python3

#
# This example uses a console buffer implementation to perform fast rendering of text.
# Performance measurements are displayed.
# Performance might vary greatly from system to system.
#



import os
import sys
import time
import datetime
import traceback

from jk_console import *
from jk_console.viewport import *




frame_colBG = ViewPortRGB.parseCSS("#000000")
frame_colFG = ViewPortRGB.parseCSS("#c0c0c0")


chars = ".,;/;,. "
colors = [
	ViewPortRGB.parseCSS("#808080"),
	ViewPortRGB.parseCSS("#8080c0"),
	ViewPortRGB.parseCSS("#8080ff"),
	ViewPortRGB.parseCSS("#c0c0ff"),
	ViewPortRGB.parseCSS("#ffffff"),
	ViewPortRGB.parseCSS("#c0c0ff"),
	ViewPortRGB.parseCSS("#8080ff"),
	ViewPortRGB.parseCSS("#8080c0"),
]
w = Console.width()
h = Console.height()
mods = [ 0, -1, -1, -2, -2, -1, -1, 0 ]

vp = ViewPort()
cb = None
bForProfiling = True



def init():
	global w, h, vp, cb

	cb = vp.createBuffer(0, 0, w, h - 1)

	rect = Rect(0, 0, cb.width, cb.height)
	rect = rect.shrink(right = 1, bottom = 1)

	cb.drawRect((rect.x, rect.y, rect.width, rect.height), colBG=frame_colBG, colFG=frame_colFG)

	w = cb.width
	h = cb.height
#

def drawPattern(cb:ConsoleBuffer, ofs:int):
	for iy in range(1, h - 2):
		for ix in range(2, w - 2):
			j = (iy + ofs) % 8
			i = (ix + iy + ofs + mods[j]) % 8
			cb.set(ix, iy, chars[i], colFG=colors[i])
#

try:
	init()

	drawPattern(cb, 0)
	i = 1
	while not bForProfiling or (i < 200):
		#time.sleep(0.05)

		t0 = datetime.datetime.now()
		drawPattern(cb, i)
		t1 = datetime.datetime.now()
		vp.render()
		t2 = datetime.datetime.now()

		#time.sleep(0.001)

		td1 = t1 - t0
		td2 = t2 - t1
		tdS = t2 - t0
		pdata = [
			"~~ screen-size: ", str(w), "x", str(h), " pixels"
			" ~~ rendering: %d.%03ds" % (td1.seconds, (td1.microseconds + 499) // 1000),
			" ~~ buffer-to-screen: %d.%03ds" % (td2.seconds, (td2.microseconds + 499) // 1000),
			" ~~ total: %d.%03ds (fps %d)" % (tdS.seconds, (tdS.microseconds + 499) // 1000, int(1.0 / (t2 - t0).total_seconds())),
		]
		if bForProfiling:
			pdata.append(" ~~ " + str(199-i))
		pdata.append(" ~~")
		cb.drawText((2, h - 2), text="".join(pdata), colFG=frame_colFG)
		vp.render()
		i += 1

		#ww = Console.width() - 1
		#hh = Console.height() - 1
		#if (ww != w) or (hh != h):
		#	init()
except Exception as e:
	os.system("clear")
	Console.clear()
	print(Console.RESET)
	traceback.print_exc()
