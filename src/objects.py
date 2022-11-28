class Biochar:
	def __init__(self, pH = 1, volatiles_percent = 1 , ash_percent = 1, bulk_density = 0.6, specific_surface_area = 1, pore_volume = 1):
		self.pH = pH 
		self.volatiles_percent = volatiles_percent
		self.ash_percent = ash_percent
		self.BulkDensity = bulk_density
		self.specific_surface_area = specific_surface_area
		self.pore_volume = pore_volume

class Soil:
	def __init__(self, N = 1, P = 5, K = 1, C = 1,  pH = 1, bulkDensity = 1.5, depth = 30):
		self.pH = pH 
		self.N = N 
		self.P = P # mg / m^2
		self.K = K 
		self.C = C
		self.Depth = depth #cm
		self.BulkDensity = bulkDensity
		# self.particle_density
		# self.pore_space

class DesiredSoil:
	def __init__(self, N = 1, P = 5, K = 1, C = 1, Humidity = 1, pH = 1, bulkDensity = 1.5, depth = 30):
		self.pH = pH 
		self.N = N 
		self.P = P # mg / m^2
		self.K = K 
		self.C = C
		self.Depth = depth
		self.BulkDensity = bulkDensity
		# self.particle_density
		# self.pore_space	 
