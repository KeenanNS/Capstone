import math 
from input_format import SingleDataPoint
import numpy as np 
from scipy import interpolate
import matplotlib.pyplot as plt
from calculator import Calculator
from objects import Biochar, Soil, DesiredSoil
import matplotlib.pyplot as plt

#static class just for namesake
class Backend:
	def __init__(self, CompletedDataGenerator):
		self.CompletedDataGenerator = CompletedDataGenerator
		min_x = self.CompletedDataGenerator.BottomLeftCoord[0] 
		max_x = min_x + self.CompletedDataGenerator.MapWidthDeg 
		min_y = self.CompletedDataGenerator.BottomLeftCoord[1] 
		max_y = min_y + self.CompletedDataGenerator.MapHeightDeg
		xx = np.linspace(min_x, max_x)
		yy = np.linspace(min_y, max_y)
		self.CompletedDataGenerator.xx, self.CompletedDataGenerator.yy = np.meshgrid(xx, yy)

	def RasterizeFromFakeData(self):
		# This is an important part of the picture
		calculatedPrescription = []

		C = Calculator(Biochar())

		rasterizedN = self.cheater_interpolation(self.CompletedDataGenerator.Values['N'])
		rasterizedP = self.cheater_interpolation(self.CompletedDataGenerator.Values['P'])
		rasterizedK = self.cheater_interpolation(self.CompletedDataGenerator.Values['K'])
		rasterizedC = self.cheater_interpolation(self.CompletedDataGenerator.Values['C'])
		rasterizedBulkDensity = self.cheater_interpolation(self.CompletedDataGenerator.Values['BulkDensity'])

		for i in range(len(rasterizedN)):
			n = rasterizedN[i]
			p = rasterizedP[i]
			k = rasterizedK[i]
			c = rasterizedC[i]
			BD = rasterizedBulkDensity[i]
			# these values will be passed to Prescribe
			calculatedPrescription.append(C.Prescribe(Soil(P = p, N = n, bulkDensity = BD), DesiredSoil()))

			

		print(len(calculatedPrescription))
		return calculatedPrescription

	def DemonstrateInterpolation(self):
		n = self.CompletedDataGenerator.Values['N']
		p = self.CompletedDataGenerator.Values['P']
		BD = self.CompletedDataGenerator.Values['BulkDensity']
		coords = self.CompletedDataGenerator.coordinates
		demovals = []

		C = Calculator(Biochar())
		for i in range(len(n)):
			demovals.append(C.Prescribe(Soil(P = p[i].Value, N = n[i].Value, bulkDensity = BD[i].Value), DesiredSoil()))

		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.scatter([coord[0] for coord in self.CompletedDataGenerator.coordinates], [coord[1] for coord in self.CompletedDataGenerator.coordinates], c = demovals)

		plt.show()

	def cheater_interpolation(self, points):
		x = [point.Coordinates[0] for point in points]
		y = [point.Coordinates[1] for point in points]
		z = [point.Value for point in points]
		vals = interpolate.griddata((x, y), z, (self.CompletedDataGenerator.xx.ravel(), self.CompletedDataGenerator.yy.ravel()))
		print(vals.shape)
		return vals

	def Rasterize(MapWidth, MapHeight, BottomLeft, KnownValues, DesiredGranularity):
		widthSteps = MapWidth / DesiredGranularity
		heightSteps = MapHeight / DesiredGranularity
		points = []
		for x in range(widthSteps):
			for x in range(heightSteps):
				X = BottomLeft[0] + x * DesiredGranularity
				Y = BottomLeft[1] + y * DesiredGranularity

				points.Append(InterpolateOnePoint([X, Y], KnownValues, -1/2))
		
#naive implementation, don't feel like optimizing this. Query list should be a list of SingleDataPoints
	def GetNClosestPoints(ValueOrigin, QueryList, N): 
		assert(shape(QueryList)[0] == 2)

		distList = []
		pointList = []

		for point in QueryList:
			xDist = point.coordinates[0] - ValueOrigin[0]
			yDist = point.coordinates[1] - ValueOrigin[1]
			dist = math.sqrt(math.pow(xDist, 2), math.pow(yDist, 2))
			if(len(distList < N)):
				distList.append(dist)
				pointList.append(point)
			else:
				current_max = max(distList)
				if(dist < current_max):
					idx = distList.index(current_max)
					distList[idx] = dist
					pointList[i] = point

# should return a list of SingleDataPoints which are closest to ValueOrigin
		return pointList

	# Interpolation kernel
	def StepWiseFunction(self, x, a):
	    
	    if (abs(x) >= 0) and (abs(x) <= 1):
	        return (a+2)*(math.pow(abs(x),3))-(a+3)*(math.pow(abs(x),2))+1
	        
	    elif (abs(x) > 1) & (abs(x) <= 2):
	        return a*(math.pow(abs(x), 3))-(5*a)*(math.pow(abs(x),2))+(8*a)*abs(x)-4*a
	    return 0

	def InterpolateOnePoint(self, TargetCoordinates, KnownDataPoints, coef):
		matrixA = np.matrix([self.StepWiseFunction(knownPoint.Coordinates[0], coef) for knownPoint in KnownDataPoints])
		matrixB = np.matrix([knownPoint.Value for knownPoint in KnownDataPoints])
		matrixC = np.matrix([self.StepWiseFunction(knownPoint.Coordinates[1], coef) for knownPoint in KnownDataPoints])
		targetValue = np.dot(np.dot(matrixA, matrixB), matrixC)
		return SingleDataPoint(TargetCoordinates, targetValue)

