import random as rand
import numpy as np
import matplotlib.pyplot as plot

class DataGenerator:
	def __init__(self, mapWidth, mapHeight, mapCenterPoint, mapResolution, averageN = 5, averageP = 0.6, averageK = 2, averageC = 50, averageHumidity = 25):
		self.N = averageN
		self.P = averageP
		self.K = averageK
		self.C = averageC
		self.Humidity = averageHumidity
		self.MapWidthM = mapWidth
		self.MapWidthDeg = mapWidth * mapResolution
		self.MapHeightM = mapHeight
		self.MapHeightDeg = mapHeight * mapResolution
		self.MapCenterPointDeg = mapCenterPoint
		self.MapResolution = mapResolution
		self.BottomLeftCoord = self.CalculateBottomLeft()
		self.NoiseyValueEveryOther = True
		self.NPoints = []
		self.PPoints = []
		self.KPoints = []
		self.CPoints = []
		self.HumidityPoints = []

	def CalculateBottomLeft(self):
		x = self.MapCenterPointDeg[0] - (self.MapWidthDeg / 2)
		y = self.MapCenterPointDeg[1] - (self.MapHeightDeg / 2)
		return [x,y]

	def GenRandomCoordinate(self):
		x =  self.BottomLeftCoord[0] + (self.MapWidthDeg - self.BottomLeftCoord[0]) * rand.random()
		y =  self.BottomLeftCoord[1] + (self.MapHeightDeg - self.BottomLeftCoord[1]) * rand.random()
		return [x,y]

	def GetNoiseyValue(self, N):
		if(self.NoiseyValueEveryOther):
			self.NoiseyValueEveryOther = False
			return (N * rand.random()) + N
		else:
			self.NoiseyValueEveryOther = True
			return (N * rand.random() - N)

	def GenerateValues(self, N):
		self.Count = N
		for i in range(N):
			self.NPoints.append([self.GetNoiseyValue(self.N), self.GenRandomCoordinate()])
			self.PPoints.append([self.GetNoiseyValue(self.P), self.GenRandomCoordinate()])
			self.KPoints.append([self.GetNoiseyValue(self.K), self.GenRandomCoordinate()])
			self.CPoints.append([self.GetNoiseyValue(self.C), self.GenRandomCoordinate()])
			self.HumidityPoints.append([self.GetNoiseyValue(self.Humidity), self.GenRandomCoordinate()])

	def ShowPlot(self):
		for i in range(self.Count):
			plot.scatter(self.NPoints[i][1][0], self.NPoints[i][1][1])
			plot.scatter(self.PPoints[i][1][0], self.PPoints[i][1][1])
			plot.scatter(self.KPoints[i][1][0], self.KPoints[i][1][1])
			plot.scatter(self.CPoints[i][1][0], self.CPoints[i][1][1])
			plot.scatter(self.HumidityPoints[i][1][0], self.HumidityPoints[i][1][1])
		plot.show()


generator = DataGenerator(15, 10, [45.9210874, 45.29384751], 100)
generator.GenerateValues(20)
generator.ShowPlot()
