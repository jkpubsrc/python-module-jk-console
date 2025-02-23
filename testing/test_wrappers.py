

import os
import typing

import jk_typing
#import jk_utils
import jk_logging
import jk_json
import jk_prettyprintobj
import jk_mathexpr
import jk_testing2

from jk_console.wrappers import *





with jk_logging.wrapMain() as log:

	print()

	for _function in [
			bold,
			italic,
			underline,
		]:
		_sStyle = _function.__name__
		print("STYLE " + _sStyle.upper() + ":")
		print("\t" + _function(f"This is {_sStyle}.") + f" This is normal text.")
		print()

	print()
	print()

	for _function in [
			stdBlack,
			stdBlue,
			stdGreen,
			stdCyan,
			stdRed,
			stdPurple,
			stdDarkYellow,
			stdLightGray,
			stdDarkGray,
			stdLightBlue,
			stdLightGreen,
			stdLightCyan,
			stdLightRed,
			stdLightPurple,
			stdYellow,
			stdWhite,
		]:
		_sColor = _function.__name__
		print("STD COLOR " + _sColor.upper() + ":")
		print("\t" + _function(f"This is {_sColor}.") + f" This is normal text.")
		print()

	print()
	print()

	for _functionList in [
			[	black,		darkGray,		gray,		lightGray,		white,	],
			[	darkRed,			red,			lightRed,	],
			[	darkOrange,			orange,			lightOrange,	],
			[	darkYellow,			yellow,			lightYellow,	],
			[	darkYellowGreen,	yellowGreen,	lightYellowGreen,	],
			[	darkGreen,			green,			lightGreen,	],
			[	darkGreenCyan,		greenCyan,		lightGreenCyan,	],
			[	darkCyan,			cyan,			lightCyan,	],
			[	darkCyanBlue,		cyanBlue,		lightCyanBlue,	],
			[	darkBlue,			blue,			lightBlue,	],
			[	darkBlueViolet,		blueViolet,		lightBlueViolet,	],
			[	darkViolet,			violet,			lightViolet,	],
			[	darkVioletRed,		violetRed,		lightVioletRed,	],
		]:
		_sColors = [ _fn.__name__.upper() for _fn in _functionList ]
		print("RGB COLOR " + ", ".join(_sColors) + ":")
		output = []
		for _fn in _functionList:
			output.append(_fn(f"This is {_fn.__name__}."))
		output.append("This is normal text.")
		for line in output:
			print("\t" + line)
		print()





