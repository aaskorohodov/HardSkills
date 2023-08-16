import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')


class SomeError(Exception):
    """Simple custom error class"""

    def __init__(self, error_description):
        self.error_description = error_description

    def __str__(self):
        return self.error_description


class PlotMaker:
    """Too broad class for drawing different figures and plots"""

    def __init__(self, x: list[int], y: list[int]) -> None:
        self.x = x
        self.y = y

    def show_plot(self):
        """Checks if coordinates are correct, then draws your plot"""

        if len(self.x) != len(self.y):
            raise SomeError('x and y lists must be of equal size!')
        plt.plot(self.x, self.y)
        plt.show()

    def show_triangle(self) -> None:
        """Checks if coordinates are correct, then draws triangle"""

        if len(self.x) != 4 or len(self.y) != 4:
            raise SomeError('Wrong number of coordinates! For triangle 4 coordinates require!')
        if len(self.x) != len(self.y):
            raise SomeError('x and y lists must be of equal size!')
        if self.x[0] != self.x[-1] or self.y[0] != self.y[-1]:
            raise SomeError('First and last coordinates must be at the same point, otherwise no triangle can be made!')
        plt.plot(self.x, self.y)
        plt.show()

    def show_square(self):
        """Checks if coordinates are correct, then draws square"""

        if len(self.x) != 5 or len(self.y) != 5:
            raise SomeError('Wrong number of coordinates! For square 5 coordinates require!')
        if len(self.x) != len(self.y):
            raise SomeError('x and y lists must be of equal size!')
        if self.x[0] != self.x[-1] or self.y[0] != self.y[-1]:
            raise SomeError('First and last coordinates must be at the same point, otherwise no square can be made!')
        plt.plot(self.x, self.y)
        plt.show()


a = PlotMaker([1, 5, 3, 1], [1, 3, 5, 1])
a.show_triangle()
a.show_square()
