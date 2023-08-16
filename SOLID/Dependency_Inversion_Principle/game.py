import random
import itertools

from abc import ABC, abstractmethod
from turtle import *

from Dependency_Inversion_Principle.world_creation import WorldMaker


class AbstractObject(Turtle, ABC):
    """Contract for creating objects"""

    init_height: int                # initial height of object, when animation begins
    grav: float                     # gravity, affects speed of fall
    y_speed: float                  # speed of vertical movement (up and down)
    x_speed: float                  # speed of horizontal movement (left and right)
    max_speed: float                # speed, that object gained, when first hit the ground
    angle: int                      # angle, to which object will be rotated (0 = no rotation)
    first_touch: bool = False       # True, after object hits ground at the first time

    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def contact(self, wall=False, ground=False):
        """Action to perform, when hitting wall or ground

        Args:
            wall: True, if object hit any wall
            ground: True, if object hit the ground"""
        pass

    def colour_random(self) -> None:
        """Changes self-colour to random"""

        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r, g, b)


class TurtleObject(AbstractObject):
    def __init__(self, size):
        super().__init__()
        self.init_height = size
        self.hideturtle()
        self.shape('turtle')
        self.up()
        self.grav = random.randint(1, 30) * 0.01
        self.y_speed = 0
        self.x_speed = random.random() * random.choice([-1, 1])
        self.goto(0, self.init_height)
        self.colour_random()
        self.max_speed = 0
        self.showturtle()
        self.angle = random.randint(-5, 5)
        self.first_touch = True

    def contact(self, wall=False, ground=False):
        if wall:
            self.colour_random()


class ArrowObject(AbstractObject):
    def __init__(self, size):
        super().__init__()
        self.init_height = size - 20
        self.hideturtle()
        self.shape('arrow')
        self.up()
        self.grav = random.randint(1, 30) * 0.01
        self.y_speed = 0
        self.x_speed = random.random() * random.choice([-1, 1])
        self.goto(0, self.init_height)
        self.colour_random()
        self.max_speed = 0
        self.showturtle()
        self.angle = random.randint(-5, 5)
        self.first_touch = True

    def contact(self, wall=False, ground=False):
        if ground:
            self.angle = 2
            self.left(self.angle)
        if wall:
            self.angle = 5
            self.right(self.angle)


class CircleObject(AbstractObject):
    def __init__(self, size):
        super().__init__()
        self.init_height = size - 35
        self.hideturtle()
        self.shape('circle')
        self.up()
        self.grav = random.randint(1, 30) * 0.01
        self.y_speed = 0
        self.x_speed = random.random() * random.choice([-1, 1])
        self.goto(0, self.init_height)
        self.colour_random()
        self.max_speed = 0
        self.showturtle()
        self.angle = random.randint(-5, 5)
        self.first_touch = True

    def contact(self, wall=False, ground=False):
        if ground:
            self.turtlesize(2, 2)
        if wall:
            self.turtlesize(1, 1)


class App:
    def __init__(self,
                 objects: list[AbstractObject],
                 size: int):

        world_maker = WorldMaker(len(objects))
        self.objects: list[AbstractObject] = objects
        self.window: TurtleScreen = world_maker._make_window()
        self.border: int = world_maker.make_borders(size=size, window=self.window)

    def run(self):
        while True:
            self.window.update()

            for object in self.objects:

                # spinning object left, adding vertical speed, placing it into new coordinates
                object.left(object.angle)
                object.y_speed = object.y_speed - object.grav
                object.goto(object.xcor() + object.x_speed, object.ycor() + object.y_speed)

                # it hits ground
                if object.ycor() <= -self.border:
                    # it was first ever touch of the ground
                    if object.first_touch:
                        object.max_speed = object.y_speed * -1
                        # setting object to the border coords, so that it would not wall through and stuck
                        object.sety(-self.border)
                        object.y_speed *= -1
                        object.first_touch = False
                    else:
                        object.sety(-self.border)
                        object.y_speed = object.max_speed
                    object.contact(ground=True)

                # it hits walls
                elif object.xcor() <= -self.border or object.xcor() >= self.border:
                    if object.xcor() < 0:
                        object.setx(-self.border)
                    else:
                        object.setx(self.border)
                    object.x_speed *= -1
                    object.contact(wall=True)


if __name__ == '__main__':
    map_size = 350
    # making objects
    turtles = [TurtleObject(map_size) for t in range(20)]
    circles = [CircleObject(map_size) for c in range(10)]
    arrows = [ArrowObject(map_size) for a in range(15)]
    # placing them into one list
    all_objects = list(itertools.chain(turtles, circles, arrows))
    # feeding objects into app
    app = App(all_objects, map_size)
    app.run()
