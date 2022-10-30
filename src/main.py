from generate_fake_data import DataGenerator

generator = DataGenerator(15, 10, [45.9210874, 45.29384751], 100)
generator.GenerateValues(20)

from backend import Backend 
B = Backend()
points = B.RasterizeFromFakeData(generator, 10)

print(points[0].Coordinates, points[0].Value)
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

xs = [point.Coordinates[0] for point in points]
ys = [point.Coordinates[1] for point in points]
zs = [point.Value for point in points]
ax.scatter(xs, ys, zs)
plt.show()
