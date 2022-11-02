class Biochar:
	def __init__(self, pH, volatiles_percent, ash_percent, bulk_density, specific_surface_area, pore_volume):
		self.pH = pH 
		self.volatiles_percent = volatiles_percent
		self.ash_percent = ash_percent
		self.bulk_density = bulk_density
		self.specific_surface_area = specific_surface_area
		self.pore_volume = pore_volume

class Soil:
	def __init__(self, pH, N, P, K, Humidity):
		self.pH = pH 
		self.N = N 
		self.P = P 
		self.K = K 
		self.Humidity = Humidity 
		 
