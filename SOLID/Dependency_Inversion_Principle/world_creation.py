import turtle
from turtle import TurtleScreen


class WorldMaker:
    """Responsible for creating window, map and borders. Also stores shapes, for no reason."""

    SHAPES = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

    def __init__(self, objects_in_game: int):
        """Mainly decides, how fast to boost the game, depending on number of objects."""

        self.objects = objects_in_game
        self.refresh_rate = self.objects * 6

    def make_window(self) -> TurtleScreen:
        window = turtle.Screen()
        window.tracer(self.refresh_rate)
        return window

    def make_borders(self, size: int, window: TurtleScreen) -> int:
        if size < 100:
            raise ArithmeticError('Size must be at least 100')

        border = turtle.Turtle()
        border.speed(0)
        border.hideturtle()
        border.color('red')
        border.up()
        border.pensize(5)
        border.goto(size, size)
        border.down()
        border.goto(size, -size)
        border.goto(-size, -size)
        border.goto(-size, size)
        window.update()

        return size - 10
