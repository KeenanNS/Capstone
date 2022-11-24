from input_format import CompleteInput, MultiplePointsSingleMetric, SingleDataPoint
from objects import Biochar, Soil
import random
import numpy as np

class Calculator:
	def __init__(self, biocharInput):
		self.BiocharQualities = biocharInput

	def CalculateApplicationByDepthAndPercent(self, percentage):
		return self.SoilSample.BulkDensity * self.SoilSample.Depth * 100 * 100 * percentage / 100

	def CalculateApplicatonPercentByAmmount(self, amount):
		return amount / self.SoilSample.BulkDensity / self.SoilSample.Depth / 100 / 100 * 100

	def EffectiveNPK(self):
		total = self.SoilSample.N + self.SoilSample.P + self.SoilSample.K

		n_frac = self.SoilSample.N / total
		p_frac = self.SoilSample.P / total
		k_frac = self.SoilSample.K / total

		amounts = [self.SoilSample.N, self.SoilSample.P, self.SoilSample.K]
		effective_fractions = [0.2, 0.4, 0.4]

		ratios = [n_frac / 0.2, p_frac / 0.4, k_frac / 0.4]

		smallest = 0

		for i in range(1, len(ratios)):
			if ratios[i] < ratios[smallest]:
				smallest = i

		effective_total = amounts[smallest] / effective_fractions[smallest]

		result = [effective_total * effective_fractions[i] for i in range(len(effective_fractions))]
		return result

	def CalculateRequiredRationalIncrease(self, delta, value):
		return delta / value * 100

	def CalculateQuadraticRoots(self, a, b, c):
		top_a = -b + np.sqrt((b ** 2) - 4 * a * c)
		top_b = -b - np.sqrt((b ** 2) - 4 * a * c)
		return top_a / (2 * a), top_b / (2 * a)

	def GetbiocharApplicationForDesiredPhosphorusIncrease(self, desired_increase):
		#Kg/m^2 and percent
		# this equation is a binomial line of best fit for the relationship between biochar application and the increase in Phosphorus by percent
		# the soils with low initial phosphorus saw the greatest effective increase in Phosphorus

		#y = 35.74157 + 5.874157 * (X) + 4.65618 * (X ** 2)
		root_a, root_b = self.CalculateQuadraticRoots(35.74 - desired_increase, 5.874, 4.656)

		# we care about the increasing side of this function
		return max(root_a, root_b)

	def PhosphorusContentPercentIncreaseByInitialContent(self):
		# There is a relationship between the amount of increase in Phosphorus and the initial amount of phosphorus 
		# that we could take into account. Not using it at this time though
		#mg/M^2 and percent

		return 131.6667 - 7 * self.SoilSample.P + 0.133333 * (self.SoilSample.P ** 2)

	def CalculatePhosphorusDiscrepency(self):
		delta = self.TargetSoil.P - self.SoilSample.P

		if delta < 0: return 0

		return delta

	def PrescribeBiocharBasedOnPhosphorus(self):
		delta = self.CalculateRequiredRationalIncrease(self.CalculatePhosphorusDiscrepency(), self.SoilSample.P)
		return self.GetbiocharApplicationForDesiredPhosphorusIncrease(delta)

############################################## NITROGEN #########################################

	def GetbiocharApplicationForDesiredNitrogenIncrease(self, desired_increase):
		# the relationship between nitrogen and biochar is stepwise

		if desired_increase < 40: 
			return 0.5
		else:
			return 40

	def CalculateNitrogenDiscrepency(self):
		delta = self.TargetSoil.N - self.SoilSample.N

		if delta < 0: return 0

		return delta

	def PrescribeBiocharBasedOnNitrogen(self):
		delta = self.CalculateRequiredRationalIncrease(self.CalculateNitrogenDiscrepency(), self.SoilSample.N)
		return self.GetbiocharApplicationForDesiredNitrogenIncrease(delta)

######################################## BULK DENSITY ##############################################

	def BDAmountByDeltaFull(self, delta):
		return self.BDApplicationAmountByDelta(delta - 0.328) / (-0.2367)
	return -5.6 * percent + 2.5

	def BDApplicationAmountByDelta(self, delta):

		return self.CalculateApplicationByDepthAndPercent((delta - 2.5) / (-5.6))

	def BDCalculateDelta(self):
		return self.TargetSoil.BulkDensity - self.SoilSample.BulkDensity

	def PrescribeBiocharForBD(self):
		return self.BDAmountByDeltaFull(self.BDCalculateDelta())
############ end Carbon ##########################

############ph etc###########
	def Prescribe(self, soilValues, desiredSoilValues):
		self.SoilSample = soilValues
		self.TargetSoil = desiredSoilValues
		
		P_prescription = self.PrescribeBiocharBasedOnPhosphorus()
		N_prescription = self.PrescribeBiocharBasedOnNitrogen()
		BD_prescription = self.PrescribeBiocharForBD()

		return 0 * P_prescription + 0 * N_prescription + 1 * BD_prescription