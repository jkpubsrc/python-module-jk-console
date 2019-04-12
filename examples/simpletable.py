#!/usr/bin/env python3


import os
import sys

from jk_console import *




t = SimpleTable()

with t.addRow("Key", "Value") as r:
	r.color = Console.ForeGround.STD_LIGHTGREEN
	#r.halign = SimpleTable.HALIGN_LEFT
	r.case = SimpleTable.CASE_UPPER
	r.hlineAfterRow = True

t.addRow("Country", "Germany")
t.addRow("State", "Berlin")
t.addRow("Area", "891.7 km2 ")
t.addRow("State", "Berlin")
t.addRow("Elevation", "34 m")
t.addRow("Population", "3,748,148")
t.addRow("Website", "www.berlin.de")[1].color = Console.ForeGround.STD_LIGHTCYAN

with t.column(0) as c:
	c.color = Console.ForeGround.STD_WHITE
	c.halign = SimpleTable.HALIGN_RIGHT
	c.vlineAfterColumn = True

t.column(0).color = Console.ForeGround.STD_LIGHTBLUE

print()
print(t.raw())
print()
t.print(prefix = "\t")
print()




