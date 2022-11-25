import numpy as np
class CompleteInput:
	def __init__(self, dictionary):
		self.InputDictionary = dictionary
		
class MultiplePointsSingleMetric:
	def __init__(self, singleDataPoints):
		self.Inputs = singleDataPoints
		self.Coordinates = [point.Coordinates for point in singleDataPoints]
		self.Values = [point.Value for point in singleDataPoints]

class SingleDataPoint:
	def __init__(self, coordinates, Value):
		self.Coordinates = coordinates
		self.Value = Value
