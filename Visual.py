import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Visualizations:
    def __init__(self):
        pass

    @staticmethod
    def colorizer(x, y):
        r = min(1, 1 - y / 3)
        g = min(1, 1 + y / 3)
        b = 1 / 4 + x / 16
        return (r, g, b)

    def plot_figure(self, figure, transformed_figure, original_label, transformed_label):
        plt.figure()
        plt.plot(figure[:, 0], figure[:, 1], 'bo-', label=original_label)
        plt.plot(transformed_figure[:, 0], transformed_figure[:, 1], 'ro-', label=transformed_label)
        plt.legend()
        plt.show()


    def plot_comparison(self, figure1, transformed_figure1, label1, figure2, transformed_figure2, label2):
        plt.figure()
        plt.subplot(121)
        plt.plot(figure1[:, 0], figure1[:, 1], 'bo-', label=label1[0])
        plt.plot(transformed_figure1[:, 0], transformed_figure1[:, 1], 'ro-', label=label1[1])
        plt.legend()
        plt.subplot(122)
        plt.plot(figure2[:, 0], figure2[:, 1], 'bo-', label=label2[0])
        plt.plot(transformed_figure2[:, 0], transformed_figure2[:, 1], 'ro-', label=label2[1])
        plt.legend()
        plt.show()

    def plot_cube(self, cube, alpha=0.9, color=[1, 0, 0]):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.voxels(cube, facecolors=np.array(color + [alpha]), edgecolor='k')
        plt.show()