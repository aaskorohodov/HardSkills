## Code structure

1. Script.py – entrypoint, controller
2. Handlers.py – stores Handlers classes, which creates a chain of responsibility
3. HandlersRegistration.py – stores class, responsible for automatical building of a chain

#### HandlersRegistration

This class simply parses file Handlers.py and searches any class with specific name (starts with Handler...).
Than Registrator creates instances of Handlers one by one, and register each next Handler as ... next Handler.
How it happens explained bellow.

#### Handlers

Each Handler derive from interface 'AbstractHandler'. The chain in this case must be fully completed for
correct calculation to be made. Each Handler checks if user equation is logically correct, before last
Handler simply calculates it (with eval() function).

Interface provides two important attributes for Handlers:

1. ._next – stores link onto next Handler in a chain (or onto None)
2. handle() – calls main logic of a specific Handler, in case of success – calls ._next Handler

If Handler did not find any mistakes, then its main function returns None, which means that the next Handler
can be called. If any Handler in chain found any trouble, it returns string representation of that error,
which returns through all chain up to the first Handler and to the user.

If there was no any errors in all execution precess, then the last Handler will calculate the equation and
return the result in the same way – through all Handlers.

## Pros & cons

This pattern lets you easily flow with open-close and single responsibility principles, and it's actually
pretty difficult to break them.

But on the other hand – code complexity rises exponentially. Each new Handler must be placed somewhere,
you should understand a chain, be completely sure in your interface. It looks like overengineered, especially
the part with registering new Handlers.

*'Did you do it? Yes. What did it cost? Everything.'*