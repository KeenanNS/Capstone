import pandas as pd
import seaborn as sns

import csv
import sys

from backend import Backend 

input_data = pd.read_csv(sys.argv[1])
B = Backend(input_data)
B.RasterizeFromFakeData()
B.ShowHeatMap()
B.WriteCsv('../out/' + sys.argv[2])

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

# 
# 
# 

# plt.show()