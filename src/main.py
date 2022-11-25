from generate_fake_data import DataGenerator
from input_format import MultiplePointsSingleMetric
import numpy as np
import pandas as pd
import seaborn as sns

generator = DataGenerator(15, 10, [45.9210874, 45.29384751], 100)
generator.GenerateValues(20)

from backend import Backend 
B = Backend(generator)
B.DemonstrateInterpolation()
points = B.RasterizeFromFakeData()

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(generator.xx, generator.yy, c = points)

plt.show()