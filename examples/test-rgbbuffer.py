#!/usr/bin/python3


from jk_console import *


Console.clear()

b = ConsoleBufferRGB(100, 30, bWithCaching=True)
b.fill(IntRGB.parseCSS("#808000"), IntRGB.parseCSS("#000000"), "X")
b.fillRectangle(5, 3, 20, 5, None, IntRGB.parseCSS("#ffffff"), "Y")
b.bufferToConsole(3, 3, bForceFullRepaint=True)














