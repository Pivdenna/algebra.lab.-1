import numpy as np

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

    def mirror_figure(self, figure, angle):
        alpha = np.radians(angle)
        mirror_matrix = np.array([
            [np.cos(alpha), np.sin(alpha)],
            [np.sin(alpha), -np.cos(alpha)]
        ])
        return np.dot(figure, mirror_matrix)

    def shear_x(self, figure, shear_factor):
        shear_matrix = np.array([
            [1, 0],
            [shear_factor, 1]
        ])
        return np.dot(figure, shear_matrix)

    def transform(self, figure, transformation_matrix):
        return np.dot(figure, transformation_matrix)

    def rotation_matrix_x(self, angle):
        angle_rad = np.deg2rad(angle)
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, np.cos(angle_rad), -np.sin(angle_rad)],
            [0, np.sin(angle_rad), np.cos(angle_rad)]
        ])
        return rotation_matrix

    def rotate_cube(self, cube, rotation_matrix):
        coords = np.argwhere(cube)
        center = np.mean(coords, axis=0)
        new_coords = []

        for coord in coords:
            vec = coord - center
            rotated_vec = rotation_matrix @ vec
            new_coord = np.round(rotated_vec + center).astype(int)
            new_coords.append(new_coord)

        rotated_cube = np.zeros_like(cube)
        for new_coord in new_coords:
            if all(0 <= new_coord[i] < cube.shape[i] for i in range(3)):
                rotated_cube[tuple(new_coord)] = True

        return rotated_cube

    def scaling_matrix(self, sx, sy, sz):
        matrix = [
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ]

        return np.array(matrix)

    def scale_cube(self, cube, transformation_matrix):
        coords = np.argwhere(cube)
        center = np.mean(coords, axis=0)
        new_coords = []

        for coord in coords:
            vec = np.append(coord - center, 1)
            transformed_vec = transformation_matrix @ vec
            new_coord = np.round(transformed_vec[:3] + center).astype(int)
            new_coords.append(new_coord)

        transformed_cube = np.zeros_like(cube)
        for new_coord in new_coords:
            if all(0 <= new_coord[i] < cube.shape[i] for i in range(3)):
                transformed_cube[tuple(new_coord)] = True

        return transformed_cube

