

import typing

from ..Console import Console
from ._ColoredTextChunk import _ColoredTextChunk






class ConsoleLineBuffer(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self,
			colorOverride:str|None = None,
		):
		if colorOverride is not None:
			assert isinstance(colorOverride, str)

		self.__chunks:list[_ColoredTextChunk] = []
		self.__len = 0
		self.__colorOverride = colorOverride
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def length(self) -> int:
		return self.__len
	#

	@property
	def colorOverride(self) -> str|None:
		return self.__colorOverride
	#

	@colorOverride.setter
	def colorOverride(self, value:str|None):
		if value is not None:
			assert isinstance(value, str)

		self.__colorOverride = value
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __len__(self) -> int:
		return self.__len
	#

	def __bool__(self) -> int:
		return self.__len > 0
	#

	def setColorOverride(self, colorOverride:str|None):
		if colorOverride is not None:
			assert isinstance(colorOverride, str)

		self.__colorOverride = colorOverride
	#

	def append(self, text:str, color:str|None = None, padToLen:int = -1):
		self.__chunks.append(_ColoredTextChunk(text, color))
		self.__len += len(text)

		if padToLen > 0:
			nPaddingRequired = padToLen - len(text)
			if nPaddingRequired > 0:
				self.__chunks.append(_ColoredTextChunk(" " * nPaddingRequired, None))
				self.__len += nPaddingRequired
	#

	#
	# Convert the internally stored text chunks to a string.
	#
	def toStr(self, lineLength:int) -> str:
		assert isinstance(lineLength, int)
		assert lineLength >= 0

		# ----

		chunks = self.__chunks

		nAdditional = lineLength - self.__len
		if nAdditional > 0:
			chunks = list(self.__chunks)
			chunks.append(_ColoredTextChunk(" " * nAdditional, None))

		# ----

		output = []

		if self.__colorOverride is not None:
			output.append(self.__colorOverride)
			for chunk in chunks:
				output.append(chunk.text)
			output.append(Console.RESET)
		else:
			for chunk in chunks:
				if chunk.color is not None:
					output.append(chunk.color)
					output.append(chunk.text)
					output.append(Console.RESET)
				else:
					output.append(chunk.text)

		return "".join(output)
	#

#







