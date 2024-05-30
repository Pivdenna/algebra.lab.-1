import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class Figures:
    def __init__(self):
        self.triangle = self.create_triangle()
        self.square = self.create_square()

    def create_triangle(self):
        triangle = np.array([[-1, -1], [1, -1], [0, 1], [-1, -1]])
        return triangle

    def create_square(self):
        square = np.array([[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]])
        return square

class Visualizations:
    def __init__(self):
        pass

    @staticmethod
    def colorizer(x, y):
        r = min(1, 1 - y / 3)
        g = min(1, 1 + y / 3)
        b = 1 / 4 + x / 16
        return (r, g, b)

class Functions:
    def __init__(self, rotation=None, scale=None, mirror=None, slope=None, universal=None):
        self.rotation = rotation
        self.scale = scale
        self.mirror = mirror
        self.slope = slope
        self.universal = universal

    def rotate(self, figure, angle):
        theta = np.radians(angle)
        rotation_matrix = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
        return np.dot(figure, rotation_matrix)

    def scale_figure(self, figure, scale_factor):
        scale_matrix = np.array([
            [scale_factor, 0],
            [0, scale_factor]
        ])
        return np.dot(figure, scale_matrix)



figures = Figures()
functions = Functions()
rotated_triangle = functions.rotate(figures.triangle, 45)
rotated_square = functions.rotate(figures.square, 90)
plt.figure()
plt.plot(figures.triangle[:, 0], figures.triangle[:, 1], 'bo-')
plt.plot(rotated_triangle[:, 0], rotated_triangle[:, 1], 'ro-')
plt.show()
plt.figure()
plt.plot(figures.square[:, 0], figures.square[:, 1], 'bo-')
plt.plot(rotated_square[:, 0], rotated_square[:, 1], 'ro-')
plt.show()

scaled_triangle = functions.scale_figure(figures.triangle, 2)
scaled_square = functions.scale_figure(figures.square, 0.5) 

plt.figure()
plt.subplot(121)
plt.plot(figures.triangle[:, 0], figures.triangle[:, 1], 'bo-', label='Original Triangle')
plt.plot(scaled_triangle[:, 0], scaled_triangle[:, 1], 'ro-', label='Scaled Triangle')
plt.legend()
plt.subplot(122)
plt.plot(figures.square[:, 0], figures.square[:, 1], 'bo-', label='Original Square')
plt.plot(scaled_square[:, 0], scaled_square[:, 1], 'ro-', label='Scaled Square')
plt.legend()
plt.show()