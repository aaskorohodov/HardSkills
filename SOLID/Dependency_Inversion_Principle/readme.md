```
1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.
```

# Structure

This is a simple script based on turtle library. Script consists of 2 file:

1. game.py – main script and point of entrance
2. world_creation.py – holds class, that creates the window

world_creation.py contains class WorldMaker, which responsible for creating window with and draw borders
(kinda like a 'map'). Inside game.py there is an abstract class for producing different types of objects
that would jump (literally) inside our map.

## Bad example

First, lets look at some nasty way of creating an instance – right inside another class:

```python
class App:
    def __init__(self,
                 objects: list[AbstractObject],
                 size: int):

    --> world_maker = WorldMaker(len(objects)) <--
    ...
```

Here we make our WorldMaker right inside init of the main App class. That brings us some strong dependencies 
between App and WorldMaker. That means that if we would like to change WorldMaker for some other class, that
would cause us some troubles, especially after some time, when initial WorldMaker would gain more and more
functionality and different methods (which often happens in real life situations). That would cause us problems
with catching all that places and trying not to disturb existing code too much.

## Good example

On the other hand we have different objects, inherited from abstract class AbstractObject:

```python
class AbstractObject(Turtle, ABC):
    """Contract for creating objects"""

    init_height: int                # initial height of object, when animation begins
    ...

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def contact(self, wall=False, ground=False):
        ...

    def colour_random(self) -> None:
        ...
```

This class in not fully abstract, however ABC prevents user from instantiating without implementing method
'contact' which responsible for ... action when object contact ground or walls. This is not very tight made
protocol, cause its lets us derive from it without implementing some of its attributes (all of them)
which will break out code, but I'm a bit too lazy for figuring out how to make it right. Also, its python,
where anyone can easily do whatever they want, so...

What good about that (and useful) is that user don't have to dig code too much to figure out what he needs to
make some others object, what that object should look like, which attributes and method it must implement and
how to make new object work. He or she can simply create new class, make some instances and feed it into App
class:

```python
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
```

And that's it! App does not depend on objects, and objects does not deepend on App – both of them depend on
abstract class, which establishes protocol\interface between them. It does not mean that protocol prevents
us from everything, but helps alot.