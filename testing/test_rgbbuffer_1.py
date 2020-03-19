#!/usr/bin/env python3

#
# This program tests some aspects of ConsoleBufferRGB.
#



import os
import random
import sys

from jk_console import *





Console.clear()
w, h = Console.getSize()


# --------------------------------


cbuf0 = ConsoleBufferRGB2(w//2, h//2)

rng = random.Random()
fgColor = IntRGB.parseCSS("#606060")
for x in range(0, w//2):
	for y in range(0, h//2):
		cbuf0.set(x, y, None, fgColor, rng.choice("abcdefghijklmnopqrstuvwxyz"))

cbuf0.bufferToConsole(0, 0)


# --------------------------------


cbuf1 = ConsoleBufferRGB2(4, 4, IntRGB.parseCSS("#c0c0c0"))

cbuf1.set(0, 0, None, IntRGB.parseCSS("#800000"), "A")
cbuf1.set(1, 1, None, IntRGB.parseCSS("#008000"), "B")
cbuf1.set(2, 2, None, IntRGB.parseCSS("#808080"), "C")
cbuf1.set(3, 3, None, IntRGB.parseCSS("#800080"), "D")

cbuf1.bufferToConsole(2, 2)


# --------------------------------


cbuf2 = ConsoleBufferRGB2(4, 4, IntRGB.parseCSS("#808080"))
framedBoxSettingsRGB = FramedBoxSettingsRGB()
framedBoxSettingsRGB.frameColorBG = IntRGB.parseCSS("#606060")
cbuf2.drawFrame(Rect(0, 0, 4, 4), framedBoxSettingsRGB)				# background doesn't get drawn! why? if set() is called it works!

cbuf2.bufferToConsole(2, 7)
cbuf2.bufferToConsole(8, 2)


# --------------------------------






