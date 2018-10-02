#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from jk_console import Console


def rangef(start, end, step):
	v = start
	while v <= end:
		yield v
		v += step
#



Console.clear()

for _l in rangef(0, 100, 3):
	for _h in rangef(0, 100, 0.8):
		h = _h/100.0
		l = _l/100.0
		c = Console.BackGround.hsl1(h, 1, l)
		print(c + " ", end="")
	print(Console.RESET)

print()







