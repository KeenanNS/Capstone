class Input:
	def __init__(self, dataPoints):
		self.Inputs = dataPoints

class SingleDataPoint:
	def __init__(self, coordinates, Value):
		self.Coordinates = coordinates
		self.Value = Value

class PointValue:
	def __init__(self, valueType, value):
		self.ValueType = valueType
		self.Value = value