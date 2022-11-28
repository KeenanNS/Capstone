from generate_fake_data import DataGenerator
from input_format import MultiplePointsSingleMetric
import numpy as np
import pandas as pd
import seaborn as sns

import csv
import sys
# generator = DataGenerator(15, 10, [45.9210874, 45.29384751], 100)
# generator.GenerateValues(20)
# generator.GenerateCSV()
from backend import Backend 

input_data = pd.read_csv(sys.argv[1])
B = Backend(input_data)
points = B.RasterizeFromFakeData()
B.WriteCsv(sys.argv[2])

# f = open(sys.argv[2], 'w')
# writer = csv.writer(f)

# xx, yy = generator.xx.ravel(), generator.yy.ravel()

# for i in range(len(generator.xx)):
# 	for j in range(len(generator.yy)):
# 		point = points[ (j * len(generator.xx)) + i]
# 		if point < 1000000 and point > -1000000:
# 			writer.writerow([str(generator.xx[0][i]), str(generator.yy[0][j]), str(point)])

#f.close()
# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(generator.xx, generator.yy, c = points)

# plt.show()