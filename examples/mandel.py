#!/usr/bin/python3


import math
from PIL import Image

from jk_testing import Assert
from jk_console import Console





















realIterator1 = FloatIterator(-2, 1, 0.04)				# X axis
imaginaryIterator1 = FloatIterator(-1, 1, 0.04)			# Y axis
matrix1 = ComplexSpacePixelMatrix(realIterator1, imaginaryIterator1)
matrix1.fill(255)

factorReal = 20
factorImaginary = 20

realIterator2 = FloatIterator(-2, 1, 0.04 / factorReal)				# X axis
imaginaryIterator2 = FloatIterator(-1, 1, 0.04 / factorImaginary)	# Y axis
matrix2 = ComplexSpacePixelMatrix(realIterator2, imaginaryIterator2)

ii = 0
for i in imaginaryIterator2:
	rr = 0
	for r in realIterator2:
		c = C(r, i)
		n = 0
		z = C.ZERO
		while n < 255:
			z = z.sqr() + c
			n += 1
			if z.abs() > 2:
				break

		if ((ii % factorImaginary) == 0) and ((rr % factorReal) == 0):
			matrix1.set(C(r, i), n)

		matrix2.set(C(r, i), n)
		rr += 1

	if (ii % factorImaginary) == 0:
		matrix1.printToScreen()
	ii += 1

matrix2.toImage().show()
















