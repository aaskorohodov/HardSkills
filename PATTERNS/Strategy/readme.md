# What it does

This is a small console-application, that lets user search any english word in a list of word. The result is
an index of this word in pythonic list of words. User can also (which is more important) select a search engine.
Each engine makes the same, but in different way. When a given word would be found, user will also receive see
time, spend on search. Different engines making their work in different time, which is a nice thing to observe.

## Code structure

1. Interface.py – stores an interface for creating different strategies
2. Strategies.py – strategies themselves. Each one is a class, derived from interface
3. Script .py – class of the main application and an entrypoint
4. words.txt – +400k of english words

## Overview

Strategy pattern becomes very similar to Factory, if using abstractions. Strategy itself does not force us
to use factory, it only tells to have some variations to make the same job done, but it is very obvious place
to put factory in.

Does Strategy pattern helpfully? Obviously yes – it is a natural way of writing code, if you need to have one
application or entrypoint and different options to make job done. In my example user is a deterministic factor
who drives application into one way or another, and search engines themselves are a big part of code base.

How expensive it was to use Strategy? In this particular example – not expensive at all. This part of code
makes all job, associated with creating engines:

```python
def create_engines(self) -> list[SearchEngine]:
    """Finds all classes in Strategies.py, checks if it derives from SearchEngine and initiates them all."""

    all_classes = dir(Strategies)
    search_engines = []

    for el in all_classes:
        cls = getattr(Strategies, el)

        try:
            if issubclass(cls, SearchEngine) and not cls == SearchEngine:
                search_engines.append(cls())
        except:
            pass

    return search_engines
```

It is fairly compact and can handle any new engines added. How much does it take to select an engine? Well,
most of the code does interaction with user, and part of selecting one if this:

```python
# Mapping engines with integers representation of that engine (engine1==1, engine2==2... select 1,2...)
number = 1
comparison = {}
for search_engine in self.search_engines:
    comparison[number] = search_engine
    number += 1
...
# If user typed real engine number, than it is what we need
if engine_number in comparison.keys():
    selected_engine = engine_number
```

Is there are wny cons? I don't think so. For this specific job, Strategy (especially combined with Factory)
is really useful and simple tool to make your code done. It makes code clear and separates specific worker
from main application, and all that happens without complicating your code and does not force you to imply
specific type of worker – it can be an interface or hardcoded implementation, the main idea is to select
some way of handling some task.