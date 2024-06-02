import numpy as np
class Figures:
    def __init__(self) -> object:
        self.triangle = self.create_triangle()
        self.square = self.create_square()

    def create_triangle(self):
        triangle = np.array([[-1, -1], [1, -1], [0, 1], [-1, -1]])
        return triangle

    def create_square(self):
        square = np.array([[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]])
        return square

    def create_cube(self, size):
        x, y, z = np.indices((size, size, size))
        cube = (x < size) & (y < size) & (z < size)
        return cube
