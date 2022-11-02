from generate_fake_data import DataGenerator
from input_format import MultiplePointsSingleMetric

generator = DataGenerator(15, 10, [45.9210874, 45.29384751], 100)
generator.GenerateValues(20)

from backend import Backend 
B = Backend()
input_values = MultiplePointsSingleMetric(generator.Values['N'])
points = B.RasterizeFromFakeData(generator, 10)

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(input_values.xx.ravel(), input_values.yy.ravel(), points)
plt.show()