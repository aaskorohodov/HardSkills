import time
import turtle
import random

from pygame.mixer import Sound

from PATTERNS.Observer.IngameObjects import Rockets, Ball, Count, FONT, Wow
from PATTERNS.Observer.Interfaces import Observer, Observable


class GameStarter:
    def start_game(self):
        self.window = self._make_window()
        self._make_board()
        self._make_net()
        self.player = Rockets(650)
        self._set_window()
        bot = Rockets(-650)
        ball = Ball()
        p1, p2 = self._make_count()

        return self.window, self.player, bot, ball, p1, p2

    def _make_window(self):
        window = turtle.Screen()
        window.title('Ping-Pong')
        window.setup(width=1.0, height=1.0)
        window.bgcolor('black')
        return window

    def _make_board(self):
        board = turtle.Turtle()
        board.speed(0)
        board.hideturtle()
        board.color('green')
        board.pensize(1)
        board.up()
        board.goto(700, 400)
        board.down()
        board.begin_fill()
        board.goto(700, -400)
        board.goto(-700, -400)
        board.goto(-700, 400)
        board.goto(700, 400)
        board.end_fill()

    def _make_net(self):
        net = turtle.Turtle()
        net.speed(5)
        net.shape('turtle')
        net.color('white')
        net.pensize(5)
        net.penup()
        net.goto(0, 400)
        net.pendown()
        net.right(90)
        for i in range(25):
            if i % 2 == 0:
                net.forward(32)
            else:
                net.penup()
                net.forward(32)
                net.pendown()
        net.hideturtle()

    def _make_count(self):
        p1 = Count()
        p1.setposition(-500, 400)
        p1.write(p1.count, font=FONT)
        p2 = Count()
        p2.setposition(500, 400)
        p2.write(p1.count, font=FONT)
        time.sleep(1)
        return p1, p2

    def _set_window(self):
        self.window.tracer(10)
        self.window.listen()
        self.window.onkeypress(self.player.move_up, "Up")
        self.window.onkeypress(self.player.move_down, "Down")
        self.window.onkeypress(self.player.super_hit, "space")
        self.window.onkeypress(self.player.freeze_hit, "w")


class EventsHandler(Observer):
    def __init__(self,
                 window: turtle.TurtleScreen,
                 p1: Count,
                 p2: Count,
                 player: Rockets,
                 bot: Rockets,
                 sounds: dict[str, Sound],
                 ball: Ball):

        self.window: turtle.TurtleScreen = window
        self.p1: Count = p1
        self.p2: Count = p2
        self.player: Rockets = player
        self.bot: Rockets = bot
        self.score_sound: Sound = sounds['score_sound']
        self.fail_sound: Sound = sounds['fail_sound']
        self.victory_sound: Sound = sounds['victory_sound']
        self.hit_sound: Sound = sounds['hit_sound']
        self.wall_hit_sound: Sound = sounds['wall_hit_sound']
        self.super_hit_sound: Sound = sounds['super_hit_sound']
        self.ball = ball

    def score(self):
        """Updates scores"""

        self.p1.clear()
        self.p2.clear()
        self.score_sound.play()
        self.p1.write(self.p1.count, font=FONT)
        self.p2.write(self.p2.count, font=FONT)

    def player_fail(self):
        self.p1.count += 1
        self.bot.bot_speed -= 0.3
        self.ball.ball_speed -= 0.4
        self.ball.dy = 0
        self.ball.dx = 0
        for i in range(3):
            self.fail_sound.play()
            self.ball.color('red')
            self.window.bgcolor('yellow')
            time.sleep(0.1)
            self.ball.color('white')
            self.window.bgcolor('black')
            time.sleep(0.1)
        time.sleep(1)
        self.ball.speed(5)
        self.ball.goto(0, 0)
        self.ball.speed(0)
        self.score()
        self.ball.dy = random.random() * random.choice([-1, 1])
        self.ball.dx = self.ball.ball_speed * random.choice([-1, 1])

    def player_win(self):
        self.p2.count += 1
        self.bot.bot_speed += 0.5
        self.ball.ball_speed += 0.7
        self.wow()
        time.sleep(1)
        self.ball.speed(5)
        self.ball.goto(0, 0)
        self.ball.speed(0)
        self.score()
        self.ball.dy = random.random() * random.choice([-1, 1])
        self.ball.dx = self.ball.ball_speed * random.choice([-1, 1])

    def wow(self):
        """Victory or score event"""

        self.victory_sound.play()
        self.window.tracer(20)
        wows = []
        for i in range(30):
            wow = Wow()
            wows.append(wow)

        for i in range(150):
            for wow in wows:
                wow.left(wow.angle)
                wow.y_speed = wow.y_speed - wow.grav
                wow.goto(wow.xcor() + wow.x_speed, wow.ycor() + wow.y_speed)

        self.window.tracer(10)

    def wall_hit(self):
        self.ball.dy = self.ball.dy * -1
        self.wall_hit_sound.play()

    def update_frame(self):
        """Update graphics and moves the ball"""

        self.window.update()
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def regular_hit(self):
        self.ball.dx = self.ball.dx * -1.1
        self.hit_sound.play()

    def freeze_hit(self):
        self.ball.dx = self.ball.dx / 3
        self.player.color('white')
        self.hit_sound.play()

    def super_hit(self):
        self.ball.dx = self.ball.dx * -3
        self.player.super = 0
        self.player.color('white')
        self.super_hit_sound.play()

    def bot_hit(self):
        self.ball.dx = self.ball.dx * -1.1
        self.hit_sound.play()
        self.ball.dy = random.random() * random.choice([1, -1])

    def correct_ball_position(self):

        distance = self.ball.distance(self.player)
        if self.player.ycor() < self.ball.ycor():
            self.ball.dy = (distance / 30) * -1
        else:
            self.ball.dy = (distance / 30)

    def update(self, action):
        """Decides, which method to call"""

        # If this observer has required method -> getting that method with getattr and calling it
        if hasattr(self, action):
            method_to_call = getattr(self, action)
            method_to_call()


class GameMechanics(Observable):
    def __init__(self,
                 player: Rockets,
                 bot: Rockets,
                 ball: Ball):

        super().__init__()
        self.player: Rockets = player
        self.bot: Rockets = bot
        self.ball = ball

    def run(self):
        while True:
            self.notify('update_frame')

            if self.ball.ycor() >= 395 or self.ball.ycor() <= -395:
                self.notify('wall_hit')
            elif self.ball.xcor() >= 700:
                self.notify('player_fail')
            elif self.ball.xcor() <= -700:
                self.notify('player_win')
            if self.player.ycor() - 50 <= self.ball.ycor() <= self.player.ycor() + 50 and \
                    self.player.xcor() - 10 <= self.ball.xcor() <= self.player.xcor() + 30:
                if not self.player.super and not self.player.freeze:
                    self.notify('regular_hit')
                elif self.player.freeze and not self.player.super:
                    self.notify('freeze_hit')
                else:
                    self.notify('super_hit')
                if self.player.ycor() < self.ball.ycor() or self.player.ycor() > self.ball.ycor():
                    self.notify('correct_ball_position')
            if self.bot.ycor() - 50 <= self.ball.ycor() <= self.bot.ycor() + 50 and \
                    self.bot.xcor() - 30 <= self.ball.xcor() <= self.bot.xcor() + 10:
                self.notify('bot_hit')
            if self.ball.xcor() <= 0:
                if self.bot.ycor() < self.ball.ycor():
                    self.bot.goto(self.bot.xcor(), self.bot.ycor() + self.bot.bot_speed)
                elif self.bot.ycor() > self.ball.ycor():
                    self.bot.goto(self.bot.xcor(), self.bot.ycor() - self.bot.bot_speed)
