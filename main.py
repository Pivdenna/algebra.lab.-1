import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Figures import Figures
from Functions import Functions
from Visual import Visualizations

figures = Figures()
functions = Functions()
visualizations = Visualizations()

# Rotate figures
rotated_triangle = functions.rotate(figures.triangle, 45)
rotated_square = functions.rotate(figures.square, 90)
visualizations.plot_figure(figures.triangle, rotated_triangle, 'Original Triangle', 'Rotated Triangle')
visualizations.plot_figure(figures.square, rotated_square, 'Original Square', 'Rotated Square')

# Scale figures
scaled_triangle = functions.scale_figure(figures.triangle, 3)
scaled_square = functions.scale_figure(figures.square, 0.5)
visualizations.plot_comparison(figures.triangle, scaled_triangle, ['Original Triangle', 'Scaled Triangle'],
                               figures.square, scaled_square, ['Original Square', 'Scaled Square'])

# Mirror figures
mirrored_triangle = functions.mirror_figure(figures.triangle, 31)
mirrored_square = functions.mirror_figure(figures.square, 87)
visualizations.plot_comparison(figures.triangle, mirrored_triangle, ['Original Triangle', 'Mirrored Triangle'],
                               figures.square, mirrored_square, ['Original Square', 'Mirrored Square'])

# Shear figures along x-axis
sheared_triangle_x = functions.shear_x(figures.triangle, 0.5)
sheared_square_x = functions.shear_x(figures.square, 3)
visualizations.plot_comparison(figures.triangle, sheared_triangle_x, ['Original Triangle', 'Sheared Triangle (x-axis)'],
                               figures.square, sheared_square_x, ['Original Square', 'Sheared Square (x-axis)'])

# Custom transformation
transformation_matrix = np.array([
    [5, 0],
    [0, 1]
])
transformed_triangle = functions.transform(figures.triangle, transformation_matrix)
transformed_square = functions.transform(figures.square, transformation_matrix)
visualizations.plot_comparison(figures.triangle, transformed_triangle, ['Original Triangle', 'Transformed Triangle'],
                               figures.square, transformed_square, ['Original Square', 'Transformed Square'])

#Створення куба
size = 4
cube = figures.create_cube(size)
visualizations.plot_cube(cube, alpha=0.9, color=[1, 0, 0])

# Rotate cube and plot
rotation_matrix = functions.rotation_matrix_x(90)
rotated_cube = functions.rotate_cube(cube, rotation_matrix)
visualizations.plot_cube(rotated_cube, alpha=0.9, color=[0, 0, 1])

scaling_matrix = functions.scaling_matrix(0.5, 0.5, 0.5)
scaled_cube = functions.scale_cube(cube, scaling_matrix)
visualizations.plot_cube(scaled_cube, alpha=0.9, color=[1, 0, 1])