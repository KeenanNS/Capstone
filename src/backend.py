import math 
from input_format import SingleDataPoint, PointValue
import numpy as np 
from scipy import interpolate

#static class just for namesake
class Backend:
	def __init__(self):
		pass
	def RasterizeFromFakeData(self, CompletedDataGenerator, DesiredGranularity):
		widthSteps = CompletedDataGenerator.MapWidthDeg // DesiredGranularity
		heightSteps = CompletedDataGenerator.MapHeightDeg // DesiredGranularity
		function_approximation = self.cheater_interpolation(CompletedDataGenerator.Values['N'])
		points = []
		for x in range(widthSteps):
			for y in range(heightSteps):
				X = CompletedDataGenerator.BottomLeftCoord[0] + x * DesiredGranularity
				Y = CompletedDataGenerator.BottomLeftCoord[1] + y * DesiredGranularity
				points.append(SingleDataPoint([X,Y],function_approximation(X,Y)))

				# for (key, val) in CompletedDataGenerator.Values:

				#points.append(self.InterpolateOnePoint([X, Y], CompletedDataGenerator.Values['N'], -1/2))

		return points

	def cheater_interpolation(self, points):
		xs = [point.Coordinates[0] for point in points]
		ys = [point.Coordinates[1] for point in points]
		zs = [point.Value for point in points]
		return interpolate.interp2d(xs, ys, zs)

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

