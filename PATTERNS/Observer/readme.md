## Code structure

A bit awful solution, just to illustrate observer in action:

1. IngameObjects.py – stores object, to play with
2. GameEngines.py – stores different game mechanics
3. Interfaces.py – interfaces of Observer and Observable
4. SoundDownloader.py – converts game sounds into python-object
5. PingPong.py – entrypoint

### Observable

Small absurdity, that I decided to introduce, lies in the fact, that observer does not simply make operations
in response to what it sees, but actually makes a lot of work by supporting the game process. Let's however
start with observable.

Observable has the only important method run(), which handles main logic of the game. The game itself is a
ping-pong, so main logic hides in ball movement. What this method does is tracking the ball, player and its
opponent (bot). Each frame, method run() checks if the ball gets somewhere, where any response is required,
e.g. hit player\bot rocker, wall or if the score was gained.

Observable class derives from 'Observable' interface, which provides methods to register Observers and notify
them. It is fairly simple:

```python
class Observable:
    def __init__(self):
        """_observers stores any class, that should be notified"""
        
        self._observers = []

    def notify(self, *args):
        """Notifies all observers"""
        
        for observer in self._observers:
            observer.update(*args)

    def attach(self, observer):
        """Attaches new observer to the notification system"""
        
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """You guessed it"""
        
        if observer in self._observers:
            self._observers.remove(observer)
```

This is a pythonic interface, what I mean by that, is that duck-typing lets us simply derive from it, and you
are done. This interface does not let us select whom are we going to notify – if event happened, then all
observers will be notified. But it lets us pass arguments throughout itself, which would be usefully, as you will
shortly see.

How observable uses this notification system is also pretty simple – it calls method notify() and passes
argument which shows, what has just happened:

```python
...
def run(self):
    while True:
        self.notify('update_frame')  # <--

        if self.ball.ycor() >= 395 or self.ball.ycor() <= -395:
            self.notify('wall_hit')  # <--
        elif self.ball.xcor() >= 700:
            self.notify('player_fail')  # <--
        ...
```

### Observer

Now lets take a look at the other side of that tandem – EventsHandler class, which plays the role of an Observer.
It is derived from standard interface based on ABC:

```python
class Observer(ABC):
    @abstractmethod
    def update(self, action):
        pass
```

The most cool thing here is override by the observer's method update(), take a look:

```python
def update(self, action):
    """Decides, which method to call"""

    # If this observer has required method -> getting that method with getattr and calling it
    if hasattr(self, action):
        method_to_call = getattr(self, action)
        method_to_call()
```

Now you can get the overall idea – Observable notifies all of its Observers and passes not only a name of
an action, that has just happened, but the name of the method, that required to be called. It's not too important
however, how Observer handles notification, but in this example it simply creates methods in exact synchrony
with notification parameter, which lets us reduce method update to 3 lines of code, and terminates the need
of 'updating' update method. If new notification requires to be handled by the same observer – get a new
method to handle it, and you are good to go.

I can see that we have an overgrown class of the Observer, that requires to be splited, but I'm a bit
lazy to da that, also this example exists just to show the Observer pattern.

#### Pros and cons

The main advantage here, IMHO, is even though I built two highly coupled (or cohesive, the way you look
at it) classes, which in fact can not work without each other, they are still been connected by the only
method, which itself is a part of the interface. Basically, the Observer patter lets us separate two parts
of the game engine, in the way that they do not know obout each other.

The disadvantage here is that this pattern adds unwanted complexity. It might be a good way to separate
parts of code, and in some other situation it might be helpfully, but overall I prefer to create coupling
with more simple solutions, e.g. just letting object knows about each other and directly calling required
methods, when it is actually useful.