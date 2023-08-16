The code in this repository shows the good example (IMHO) of OCP, bad example and
controversial one.

# Overall code structure

This is a simple and a bit buggy GUI calculator, made with PyQt5. It has several main
files:

1. calc.ui – template of calculator window, made with QtDesigner
2. calc_template.py – same template, but converted into python code
3. script.py – entry point and PyQt's instances
4. calc_engine.py

calc.ui is not being used anywhere in code. It's only purpose is to make visual
construction of calculator's window easier – with special software QtDesigner one
can create any window with any widgets, that PyQt5 has. After you done with creating
your window with all it's buttons, layers, labels etc. – QtDesigner lets you save
that in file.ui, which can be converted into python code with simple console command.

And that is how we get calc_template.py, which was, however, a bit modified. Its
structure is pretty simple – one function creates widgets and places them into PyQt's
window instance, second function places text on where it is required (buttons, labels)
and last function is a bad example, which I will explain a bit lower.

Script.py is a typical way of creating PyQt-window. It has instance of application
class and instance of application's window class. Application controls window, and
window controls its template, pretty easy.

Last but not least is calc_engine.py, which is, I hope, a good example of OCP. As you
can guess, calc_engine drives calculation logic.

## Bad example

Each calculator's button is a widget, which connects to its command. In a nutshell,
when button is pressed, it calls some function, which makes some action. Because
logic of buttons with number (1,2,3...9,0) is straight-forward (add number onto calc
screen), I decided to place it into template. Generally it looks like this:

```python
self.btn_0.clicked.connect(lambda: self.show_equation('0'))
self.btn_1.clicked.connect(lambda: self.show_equation('1'))
```

It all goes well, until I wanted to limit max characters, that calcs screen can handle.
What I did is simple:

```python
def show_equation(self, symbol: str) -> None:
    # We don't want to have more than 16 symbols, because it would extend calculator's window size
    if not len(text) == 16:
        text += symbol
        self.label_screen.setText(text)
```

Here we add more symbols, onto the screen, until we reached 16 characters. But later
on I understood, that we need more logic to be implemented, for example, I don't
want to see numbers with unwanted zeroes at the beginning (009 => 9). So my function
grows bigger:

```python
def show_equation(self, symbol: str) -> None:
    """Draws users input in label area (into 'calculator screen')

    Args:
        symbol: button, that was pressed"""

    text = self.label_screen.text()

    # We don't want to see numbers like '09' on the 'screen', so if text on the 'screen' is now 0 => remove 0
    if text == '0' and symbol != '.':
        self.label_screen.setText(symbol)
        return
    # We don't want to have more than 16 symbols, because it would extend calculator's window size
    if not len(text) == 16:
        if symbol == '.' and '.' in text:
            return
        text += symbol
        self.label_screen.setText(text)
```

Still not to bad, but what if some time later on I would like to add some more buttons
(maybe brackets) and it would require more logic to be implemented? That would force
me to modify show_equation function, which violates OCP.

## Good example

On the other hand we have CalcEngine class, which represents partially abstract class
from which different calculation logic can be inherited:

```python
class CalcEngine:
    """Abstract class for different calculations operators (/*-+ etc)"""

    def __init__(self, expression: str, command: str):
        self.expression:    str = expression
        self.command:       str = command
        self.result:        Optional[int] = None
        self.operators =    ['*', '/', '-', '+']

    @abstractmethod
    def calculate(self):
        pass

    def verify_rounding(self, number) -> int or float:
        ...

    def find_operator(self) -> str:
        ...
```

Idea is simple – if any additional buttons were added, you can implement new logic
by inheriting new class from CalcEngine. At the same time CalcEngine does have some
common methods, which can be used by any of its inheritors, or they can be overridden
if necessary.

IMHO this is a good example of OCP, because if we assume that calculator will only
be modified by adding new buttons, than we can pretty easily implement new logic,
without modifying existing code.

## Controversial

Controversial part is template itself. Right now if we add new buttons, we can simply
add new widget, connect it to new calculation logic and viola. But it probably won't
be that easy, especially if taking into consideration that buttons are placed into
grid and new buttons probably will ruin it and will require to make changes into
existing code.

But that would not be too much and would not change existing logic of CalcEngine,
CalcWindow and PyQt Application. Also, It's hard to predict which buttons and where
we would like to add, in which quantities and which size they would be. So overall
Template class does not seem to violate OCP (at least too much\from my point of view).