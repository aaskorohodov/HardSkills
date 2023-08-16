# Interface Segregation Principle

`Clients should not be forced to depend on methods that they do not use.`

*Robert C. Martin;*

Here I have a small bit af code, based on MatPlotLib. What it does is draw 3 things by two given
lists of coordinates:

1. any 2D-plot
2. any triangle (plot.show() function simply connects coordinates)
3. any square

Now I will present my understanding of practical implementation of Interface Segregation Principle.
I have to say that because Python has a Duck Typing, interfaces are not as solid, as in other languages.
Also, here is no strict limitations that could prevent user from overriding everything you just made.

## Bad example with ABC

```python
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
```

As you can see, here we have a simple interface, that can draw 3 types of plots. The simplest solution
to use show_triangle() method would be something like this:

```python
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
```

But, as you already guessed, this would not work, because we did not implement all 4 abstract methods
therefor an exception will occur. But this and further examples will only make sense, if we assume that
user really wants to create such a class, which would not need to draw other plots. Which we would assume.

## Bad example with NotImplementedError

This is almost the same example, but with a bit different approach. This time instead of ABS module we will
use standard NotImplementedError exception:

```python
class PlotMaker:
    """Too broad interface for drawing different figures and plots"""

    def __init__(self, x: list[int], y: list[int]) -> None:
        self.x = x
        self.y = y

    def show_plot(self):
        raise NotImplementedError()

    def show_triangle(self):
        raise NotImplementedError()

    def show_square(self):
        raise NotImplementedError()
```

At this time user will be able to create a class without implementing all of its methods and that class
would work. But this gives us a lot of mess and a bit harder to understand what this code does.


## Bad example without explicit interface

This time I will try to solve this problem by simple creating one big class, that would not be explicitly
presented as an interface. This class would be able to draw all three plots right from the box.

```python
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
```

Looks good right? Not too much, especially if we consider that it's actually becoming too hard to handle.
For example, here we have 2 lists, each of which represents one coordinate. As you already know, for
different types of figures we need different amount of coordinates, so we need to track somehow which
amount we have, otherwise we will get an exception trying to draw square with 2 dots.

Solving this and some other problems will make this code much-much bigger and harder to read. I actually
tried, but would not present you that monster, you may thank me. So, another approach would be...

## Good example

```python
class PlotMaker(ABC):
    """Interface for drawing different figures and plots"""

    @abstractmethod
    def __init__(self, x: list[int], y: list[int]) -> None:
        pass


class TriangleDrawer(PlotMaker):
    @abstractmethod
    def show_triangle(self):
        pass


class SquareDrawer(PlotMaker):
    @abstractmethod
    def show_square(self):
        pass


class JustPlot(PlotMaker):
    @abstractmethod
    def show_plot(self):
        pass
```

Here we simply have 3 interfaces, each of them dedicated to the specific role. Using them will be easier
and code would become much clearer:

```python
class TrianglePlot(TriangleDrawer):
    def __init__(self, x, y):
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
```

Ofcourse this is not a complete example cause there is no real users and cases, which might have change
the way interface is designed. But I hope this makes a point and has at least some sense.