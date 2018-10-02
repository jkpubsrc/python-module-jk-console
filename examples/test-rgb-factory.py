#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from jk_console import IntRGB


values = [
	(	IntRGB.parseCSS("#010000"),		IntRGB.rgb256(1, 0, 0),			0xff010000	),
	(	IntRGB.parseCSS("#000100"),		IntRGB.rgb256(0, 1, 0),			0xff000100	),
	(	IntRGB.parseCSS("#000001"),		IntRGB.rgb256(0, 0, 1),			0xff000001	),

	(	IntRGB.parseCSS("#100000"),		IntRGB.rgb256(16, 0, 0),		0xff100000	),
	(	IntRGB.parseCSS("#001000"),		IntRGB.rgb256(0, 16, 0),		0xff001000	),
	(	IntRGB.parseCSS("#000010"),		IntRGB.rgb256(0, 0, 16),		0xff000010	),

	(	IntRGB.parseCSS("#100"),		IntRGB.rgb256(17, 0, 0),		0xff110000	),
	(	IntRGB.parseCSS("#010"),		IntRGB.rgb256(0, 17, 0),		0xff001100	),
	(	IntRGB.parseCSS("#001"),		IntRGB.rgb256(0, 0, 17),		0xff000011	),

	(	IntRGB.parseCSS("#800"),		IntRGB.rgb256(136, 0, 0),		0xff880000	),
	(	IntRGB.parseCSS("#080"),		IntRGB.rgb256(0, 136, 0),		0xff008800	),
	(	IntRGB.parseCSS("#008"),		IntRGB.rgb256(0, 0, 136),		0xff000088	),

	(	IntRGB.parseCSS("#c00"),		IntRGB.parseCSS("#cc0000"),		0xffcc0000	),
	(	IntRGB.parseCSS("#0c0"),		IntRGB.parseCSS("#00cc00"),		0xff00cc00	),
	(	IntRGB.parseCSS("#00c"),		IntRGB.parseCSS("#0000cc"),		0xff0000cc	),

	(	IntRGB.parseCSS("#840000"),		IntRGB.rgb256(132, 0, 0),		0xff840000	),
	(	IntRGB.parseCSS("#008400"),		IntRGB.rgb256(0, 132, 0),		0xff008400	),
	(	IntRGB.parseCSS("#000084"),		IntRGB.rgb256(0, 0, 132),		0xff000084	),

	(	IntRGB.parseCSS("rgb(1,17,132)"),	IntRGB.rgb256(1, 17, 132),		0xff011184	),

	(	IntRGB.parseCSS("#ff0000"),		IntRGB.rgb1(1, 0, 0),			0xffff0000	),
	(	IntRGB.parseCSS("#00ff00"),		IntRGB.rgb1(0, 1, 0),			0xff00ff00	),
	(	IntRGB.parseCSS("#0000ff"),		IntRGB.rgb1(0, 0, 1),			0xff0000ff	),
	(	IntRGB.parseCSS("#800000"),		IntRGB.rgb1(0.503, 0, 0),		0xff800000	),
	(	IntRGB.parseCSS("#008000"),		IntRGB.rgb1(0, 0.503, 0),		0xff008000	),
	(	IntRGB.parseCSS("#000080"),		IntRGB.rgb1(0, 0, 0.503),		0xff000080	),
	(	IntRGB.parseCSS("#7f0000"),		IntRGB.rgb1(0.5, 0, 0),			0xff7f0000	),
	(	IntRGB.parseCSS("#007f00"),		IntRGB.rgb1(0, 0.5, 0),			0xff007f00	),
	(	IntRGB.parseCSS("#00007f"),		IntRGB.rgb1(0, 0, 0.5),			0xff00007f	),
]



for v1, v2, v3 in values:
	#print(v1 & 0xffffff, v2 & 0xffffff, v3 & 0xffffff)
	print(v1 == v2 == v3)
	#print()




