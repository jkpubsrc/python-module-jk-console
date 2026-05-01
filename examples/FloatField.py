import random



class FloatField(object):

	def __init__(self, width:int, height:int, defaultValue:float = 0, _data = None):
		self.width = width
		self.height = height
		if _data:
			self.data = _data
		else:
			self.data = self.__createField(width, height, defaultValue)
	#

	def __createField(self, width:int, height:int, value:float = 0):
		rows = []
		for y in range(0, height):
			cols = []
			for x in range(0, width):
				cols.append(value)
			rows.append(cols)
		return rows
	#

	@property
	def maximum(self):
		ret = self.data[0][0]
		for y in range(0, self.height):
			for x in range(0, self.width):
				v = self.data[y][x]
				if v > ret:
					ret = v
		return ret
	#

	@property
	def minimum(self):
		ret = self.data[0][0]
		for y in range(0, self.height):
			for x in range(0, self.width):
				v = self.data[y][x]
				if v < ret:
					ret = v
		return ret
	#

	def clone(self):
		rows = []
		for y in range(0, self.height):
			cols = []
			for x in range(0, self.width):
				cols.append(self.data[y][x])
			rows.append(cols)
		return FloatField(self.width, self.height, _data = rows)
	#

	def add(self, value:float, maxValue:float = 1):
		if maxValue is None:
			for y in range(0, self.height):
				for x in range(0, self.width):
					self.data[y][x] = value
		else:
			for y in range(0, self.height):
				for x in range(0, self.width):
					v = self.data[y][x] + value
					if v > maxValue:
						v = maxValue
					self.data[y][x] = v
		return self
	#

	def subtract(self, value:float, minValue:float = 0):
		if minValue is None:
			for y in range(0, self.height):
				for x in range(0, self.width):
					self.data[y][x] = value
		else:
			for y in range(0, self.height):
				for x in range(0, self.width):
					v = self.data[y][x] - value
					if v < minValue:
						v = minValue
					self.data[y][x] = v
		return self
	#

	def fill(self, value:float):
		for y in range(0, self.height):
			for x in range(0, self.width):
				self.data[y][x] = value
		return self
	#

	def fillRandom(self):
		for y in range(0, self.height):
			for x in range(0, self.width):
				self.data[y][x] = random.random()
		return self
	#

	def smooth(self, windowSize:int):
		w1 = -windowSize
		w2 = windowSize + 1
		data2 = self.__createField(self.width, self.height)
		for y in range(0, self.height):
			for x in range(0, self.width):
				sum = 0
				count = 0
				for iy in range(w1, w2):
					yy = y + iy
					for ix in range(w1, w2):
						xx = x + ix
						if (yy >= 0) and (yy < self.height) and (xx >= 0) and (xx < self.width):
							sum += self.data[yy][xx]
							count += 1
				data2[y][x] = sum / count
		self.data = data2
		return self
	#

#

