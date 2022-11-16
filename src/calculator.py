from input_format import CompleteInput, MultiplePointsSingleMetric, SingleDataPoint
from objects import Biochar, Soil
import random
import numpy as np

class Calculator:
	def __init__(self, biocharInput):
		self.BiocharQualities = biocharInput

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

################ water ################
#This section is about calculating the amount of biochar that a user would want if they only cared about water
#water discrepency is a trait of the soil, and unrelated to the biochar, however the potential for water retention
# is only relevant in the context of the soil.. ie, the second function aims to output how many grams per m^2 should be applied
# in order to achieve the ideal water retention of the soil

    #Calculate how much more water retention the soil needs 
	def CaculateWaterDiscrepency(self):
		return 0

    #Calculate the capacity of the biochar to improve the soil's water rentention per g / unit area
	def CalculateBiocharPotentialForWaterRetention(self):
		return 1

########## end water ################

############## NPK #################
# This section is about calculating the amount of biochar the user would want to apply in order to fulfill their
# optimum NPK content values. This is an aggregate so it will make a judgement based on a stepwise function of sorts so 
# that NPK are all represented and none of them fall above or below a given threshhold if possible
	
	#Calculate the aggregate discrepency for the NPK
	def CalculateNPKDiscrepency(self):
		return 0

	#Calculate g / m^2 to achieve perfect* NPK. *perfect as per discrepency
	def CalculateBiocharPotentialForNPKremediation(self):
		return 1

############ end NPK ##########################

############## Carbon #################
# This section is about calculating the amount of biochar the user would want to apply in order to fulfill their
# optimum Carbon content value.
	
	#Calculate the aggregate discrepency for the Carbon
	def CalculateCarbonDiscrepency(self):
		return 0

	#Calculate g / m^2 to achieve perfect Carbon
	def CalculateBiocharPotentialForCarbonremediation(self):
		return 1

############ end Carbon ##########################

############ph etc###########
	def Prescribe(self, soilValues, desiredSoilValues):
		self.SoilSample = soilValues
		self.TargetSoil = desiredSoilValues
		
		return self.PrescribeBiocharBasedOnPhosphorus()