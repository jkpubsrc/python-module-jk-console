#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import time

import jk_console



jk_console.Console.clear()

for bgCol, bgName in jk_console.Console.BackGround.ALL_STD_COLORS:
	for fgCol, fgName in jk_console.Console.ForeGround.ALL_STD_COLORS:
		print(fgCol + bgCol + "    BG:" + bgName + "\tFG:" + fgName + "    " + jk_console.Console.RESET)




