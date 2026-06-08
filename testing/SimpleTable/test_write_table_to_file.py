#!/usr/bin/env python3



from jk_console import *


t = SimpleTable()
t.addRow("Monday", "Tuesday", "Wednesday", "Thursday", "Friday").hlineAfterRow = True

for y in "abcdef":
	t.addRow(*[ (y+x) for x in "abcdef" ])


t.printToTextFile("output.txt")





















