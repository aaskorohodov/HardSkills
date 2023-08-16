from abc import abstractmethod, ABC

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


class SomeError(Exception):
    """Simple custom error class"""

    def __init__(self, error_description):
        self.error_description = error_description

    def __str__(self):
        return self.error_description


class PlotMaker(ABC):
    """Too broad interface for drawing different figures and plots"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def show_plot(self):
        pass

    @abstractmethod
    def show_triangle(self):
        pass

    @abstractmethod
    def show_square(self):
        pass


class TriangleDrawer(PlotMaker):
    def __init__(self, x: list[int], y: list[int]):
        if len(x) != 4 or len(y) != 4:
            raise SomeError('Wrong number of coordinates! For triangle 4 coordinates require!')
        if len(x) != len(y):
            raise SomeError('x and y lists must be of equal size!')
        if x[0] != x[-1] or y[0] != y[-1]:
            raise SomeError('First and last coordinates must be at the same point, otherwise no triangle can be made!')
        self.x = x
        self.y = y

    def show_triangle(self):
        plt.plot(self.x, self.y)
        plt.show()


a = TriangleDrawer([1, 5, 3, 1], [1, 3, 5, 1])
a.show_triangle()
