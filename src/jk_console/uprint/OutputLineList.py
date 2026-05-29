

import sys
import typing

import jk_typing
#import jk_utils
# import jk_logging
# import jk_json
# import jk_prettyprintobj
import jk_terminal_essentials
import jk_console

from .ConsoleLineBuffer import ConsoleLineBuffer






class OutputLineList(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self):
		self.__lines:list[ConsoleLineBuffer] = []
		self.__numberOfLlinesOnLastPrint = 0
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def __print(self, bPositionCursorAtStart:bool, textIO:typing.TextIO):
		termSize = jk_terminal_essentials.getTerminalSize()

		strLines = []
		for cl in self.__lines:
			strLines.append(cl.toStr(termSize.columns - 1))

		nLines = len(strLines)
		while len(strLines) < self.__numberOfLlinesOnLastPrint:
			strLines.insert(0, " " * (termSize.columns - 1))
		self.__numberOfLlinesOnLastPrint = nLines

		strLines = strLines[-termSize.lines+1:]

		for strLine in strLines:
			print(strLine)

		if bPositionCursorAtStart:
			_cpos = jk_terminal_essentials.getCursorPosition()
			cursorY = _cpos.column - len(strLines)
			assert cursorY >= 0
			jk_console.Console.moveCursorTo(0, cursorY)

		sys.stdout.flush()
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	#
	# Remove all data.
	#
	def clear(self):
		self.__lines.clear()
	#

	#
	# Add a line.
	#
	def append(self, clb:ConsoleLineBuffer):
		self.__lines.append(clb)
	#

	#
	# Create an empty line and add it.
	#
	def createAndAppend(self, colorOverride:str|None = None) -> ConsoleLineBuffer:
		clb = ConsoleLineBuffer(colorOverride=colorOverride)
		self.__lines.append(clb)
	#

	def printPrepareReprint(self):
		self.__print(True)
	#

	def printFinal(self):
		self.__print(False)
	#

#



