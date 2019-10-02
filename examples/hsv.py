#!/usr/bin/env python3




from jk_console import Console


for i in range(0, 8):
	allS = ""
	for h in [ 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 ]:
		s = Console.BackGround.hsl1(h, 1, 0.5) + " "*18 + Console.RESET
		if allS:
			allS += " "*2
		allS += s
	print(allS)
print()






