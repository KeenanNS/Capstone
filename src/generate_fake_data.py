import random as rand
import numpy as np
import matplotlib.pyplot as plot
from input_format import SingleDataPoint
import pandas as pd

class DataGenerator:
	def __init__(self, mapWidth, mapHeight, mapCenterPoint, mapResolution, averageN = 5, averageP = 0.6, averageK = 2, averageC = 50, averageBulkDensity = 1.5):
		self.N = averageN
		self.P = averageP
		self.K = averageK
		self.C = averageC
		self.BulkDensity= averageBulkDensity
		self.MapWidthM = mapWidth
		self.MapWidthDeg = mapWidth / mapResolution
		self.MapHeightM = mapHeight
		self.MapHeightDeg = mapHeight / mapResolution
		self.MapCenterPointDeg = mapCenterPoint
		self.MapResolution = mapResolution
		self.BottomLeftCoord = self.CalculateBottomLeft()
		self.NoiseyValueEveryOther = True
		self.NPoints = []
		self.PPoints = []
		self.KPoints = []
		self.CPoints = []
		self.BulkDensityPoints = []
		self.Values = {}
		self.coordinates = []
		self.df = pd.DataFrame(columns = ['x_coord', 'y_coord', 'N', 'P', 'K', 'BulkDensity'])

	def CalculateBottomLeft(self):
		x = self.MapCenterPointDeg[0] - (self.MapWidthDeg / 2)
		y = self.MapCenterPointDeg[1] - (self.MapHeightDeg / 2)
		return [x,y]

	def GenRandomCoordinate(self):
		x =  self.BottomLeftCoord[0] + (self.MapWidthDeg * rand.random())
		y =  self.BottomLeftCoord[1] + (self.MapHeightDeg * rand.random())
		return [x,y]

	def GetNoiseyValue(self, N):
		if(self.NoiseyValueEveryOther):
			self.NoiseyValueEveryOther = False
			return (N + rand.random() * 0.2 * N)
		else:
			self.NoiseyValueEveryOther = True
			return (N - rand.random() * 0.2 * N)

	def GenerateValues(self, N):
		self.Count = N
		for i in range(N):
			x, y = self.GenRandomCoordinate()
			self.df = self.df.append({'x_coord' : x ,
									'y_coord' : y,
									'N' : self.GetNoiseyValue(self.N), 
									'P' : self.GetNoiseyValue(self.P), 
									'K' : self.GetNoiseyValue(self.K), 
									'BulkDensity' : self.GetNoiseyValue(self.BulkDensity)}, ignore_index= True)


			# coord = self.GenRandomCoordinate()
			# self.coordinates.append(coord)
			# self.NPoints.append([self.GetNoiseyValue(self.N), coord])
			# SP = SingleDataPoint(coord, self.GetNoiseyValue(self.N))
			# if not 'N' in self.Values: self.Values['N'] = []
			# self.Values['N'].append(SP)

			# self.PPoints.append([self.GetNoiseyValue(self.P), coord])
			# SP = SingleDataPoint(coord, self.GetNoiseyValue(self.P))
			# if not 'P' in self.Values: self.Values['P'] = []
			# self.Values['P'].append(SP)

			# self.KPoints.append([self.GetNoiseyValue(self.K), coord])
			# SP = SingleDataPoint(coord, self.GetNoiseyValue(self.K))
			# if not 'K' in self.Values: self.Values['K'] = []
			# self.Values['K'].append(SP)

			# self.CPoints.append([self.GetNoiseyValue(self.C), coord])
			# SP = SingleDataPoint(coord, self.GetNoiseyValue(self.C))
			# if not 'C' in self.Values: self.Values['C'] = []
			# self.Values['C'].append(SP)

			# self.BulkDensityPoints.append([self.GetNoiseyValue(self.BulkDensity), coord])
			# SP = SingleDataPoint(coord, self.GetNoiseyValue(self.BulkDensity))
			# if not 'BulkDensity' in self.Values: self.Values['BulkDensity'] = []
			# self.Values['BulkDensity'].append(SP)

		self.Values = self.df

	def GenerateCSV(self):
		#df = pd.DataFrame.from_dict(self.Values)
		self.df.to_csv('demo_input_data.csv')
		exit()

	def ShowPlot(self):
		for i in range(self.Count):
			plot.scatter(self.NPoints[i][1][0], self.NPoints[i][1][1])
			plot.scatter(self.PPoints[i][1][0], self.PPoints[i][1][1])
			plot.scatter(self.KPoints[i][1][0], self.KPoints[i][1][1])
			plot.scatter(self.CPoints[i][1][0], self.CPoints[i][1][1])
			plot.scatter(self.BulkDensityPoints[i][1][0], self.BulkDensityPoints[i][1][1])
		plot.show()


# generator = DataGenerator(15, 10, [45.9210874, 45.29384751], 100)
# generator.GenerateValues(20)
# generator.ShowPlot()
