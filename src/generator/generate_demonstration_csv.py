from generate_fake_data import DataGenerator
import sys

generator = DataGenerator(15, 10, [45.9210874, 45.29384751], 100)
generator.GenerateValues(20)
generator.GenerateCSV(sys.argv[1])

