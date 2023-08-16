from turtle import Turtle
import random
import pygame

pygame.mixer.init()
super_power = pygame.mixer.Sound('sounds/super_power.mp3')
freeze = pygame.mixer.Sound('sounds/freeze.mp3')
FONT = ('Arial', 44, 'normal')


class Rockets(Turtle):
    def __init__(self, posit):
        super().__init__()
        self.speed(2)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posit, 0)
        self.bot_speed = 1
        self.freeze = 0
        self.super = 0

    def move_up(self):
        y = self.ycor() + 20
        if y > 350:
            y = 350
        self.sety(y)

    def move_down(self):
        y = self.ycor() - 20
        if y < -350:
            y = -350
        self.sety(y)

    def super_hit(self):
        self.color('red')
        self.super = 1
        self.freeze = 0
        super_power.play()

    def freeze_hit(self):
        self.freeze = 1
        self.color('blue')
        freeze.play()
        self.freeze = 1
        self.super = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.dx = random.choice([-2, 2])
        self.dy = random.choice([-1, 1])
        self.penup()
        self.ball_speed = self.dx


class Count(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color('white')
        self.penup()
        self.hideturtle()


class Wow(Turtle):
    """Confetti-like objects, that falls when player wins or hits a score"""

    def __init__(self):
        shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
        super().__init__()
        self.init_height = random.choice([i for i in range(-300, 700)])
        self.init_space = random.choice([i for i in range(-800, 800)])
        self.hideturtle()
        self.shape(random.choice(shapes))
        self.up()
        self.grav = random.randint(1, 30)
        self.y_speed = 0
        self.x_speed = random.random() * random.choice([-1, 1])
        self.goto(self.init_space, self.init_height)
        self.colour_random()
        self.showturtle()
        self.angle = random.randint(-5, 5)

    def colour_random(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r, g, b)
