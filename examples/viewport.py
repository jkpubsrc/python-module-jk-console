#!/usr/bin/python3

#
# This example demonstrates the use of ViewPort and ViewPortBuffer objects.
#



import time

from jk_console import *
from jk_console.viewport import *





vp = ViewPort()



bufferB_colBG = ViewPortRGB.parseCSS("#000080")
bufferB_colFG = ViewPortRGB.parseCSS("#ffffff")
bufferB = vp.createBuffer(50, 20, 160, 30)
bufferB.fill("/", colBG=bufferB_colBG, colFG=bufferB_colFG)
bufferB.drawRect(bufferB.sizeRect, colBG=bufferB_colBG, colFG=bufferB_colFG)
bufferB.drawText(bufferB.sizeRect.shrink(4, 2).topLeft, text="  B L U E  ")
bufferB.drawText(bufferB.sizeRect.shrink(4, 2).bottomLeft, text="  B L U E  ")

bufferG_colBG = ViewPortRGB.parseCSS("#008000")
bufferG_colFG = ViewPortRGB.parseCSS("#ffffff")
bufferG = vp.createBuffer(30, 15, 160, 30)
bufferG.fill("/", colBG=bufferG_colBG, colFG=bufferG_colFG)
bufferG.drawRect(bufferG.sizeRect, colBG=bufferG_colBG, colFG=bufferG_colFG)
bufferG.drawText(bufferG.sizeRect.shrink(4, 2).topLeft, text="  G R E E N  ")
bufferG.drawText(bufferG.sizeRect.shrink(4, 3).bottomLeft, text="  G R E E N  ")

bufferR_colBG = ViewPortRGB.parseCSS("#800000")
bufferR_colFG = ViewPortRGB.parseCSS("#ffffff")
bufferR = vp.createBuffer(10, 10, 160, 30)
bufferR.fill("O", colBG=bufferR_colBG, colFG=bufferR_colFG)
bufferR.drawRect(bufferR.sizeRect, colBG=bufferR_colBG, colFG=bufferR_colFG)
bufferR.drawText(bufferR.sizeRect.shrink(4, 2).topLeft, text="  R E D  ")
bufferR.drawText(bufferR.sizeRect.shrink(4, 2).bottomLeft, text="  R E D  ")


vp.render()


t = time.time()
nCellsRendered = 0
n = 0
for buffer in [ bufferR, bufferG, bufferB ]:

	for i in range(MAX_BRIGHTNESS, -1, -1):
		buffer._setBrightness(i)
		nCellsRendered += vp.render()
		n += 1

	for i in range(0, MAX_BRIGHTNESS + 1):
		buffer._setBrightness(i)
		nCellsRendered += vp.render()
		n += 1

dt = time.time() - t


print(Console.RESET, end="")
print("%f seconds in total." % dt)
print("%i frames in total." % n)
print("%.3f seconds per frame." % (dt / n))
print("%.3f frame rate." % (n / dt))
print("%i cells rendered." % nCellsRendered)
print("%.1f%% of screen painted per frame." % (nCellsRendered / n / Console.width() / Console.height() * 100))
print()

