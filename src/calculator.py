from input_format import CompleteInput, MultiplePointsSingleMetric, SingleDataPoint
from objects import Biochar, Soil

class Calculator:
	def __init__(self, completeInput, soilInput, biocharInput):
		self.CompleteInput = completeInput


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