This code shows a good and a bad examples of Liskov Substitution Principle.

```
It should be possible to replace an instance of a superclass 
with an instance of a subclass without causing breaking changes.
```

IMHO, LSP is the most controversial principle in Python. Originally it states that
all subclasses should be able to replace its super class, without breaking the code.
But in many cases we simply have an abstract class, that forces us to use contracts,
defined in it. And if we don't (which python allows us to), then we should consider
that programmers don't use python in a vacuum, we have IDEs which highlight mistakes
like that.

Basically, I see LSP as a prescription to use same signatures in subclasses or make
original signature wide enough (*args, **kwargs, e.q.). Also I can imagine many
situations where a contract of a method would be intentionally open on income, but
narrow on outcome therefor user would have an ability to add any arguments and fixed
return value.

Also, duck-typing gives us ability to use any class where we want, without any need
to derive something from something, which (as I see it), was not a common thing when
Mrs. Liskov invented LSP (with full respect). However, here we go...

# Overall code structure

This is a Telegram Bot, that can response to users messages of 2 types:

1. Simple message with any text
2. Commands

Command is also a symple text, but with slash – /start. Telegram-messenger
and TeleBot library threats that types of text as commands.

Bot itself is located in Telebot_Main_Engine.py. It has a very simple structure:

1. We initiating our bot class and giving it a token, that we got from another
bot named BothFather
2. Creating our function for different users messages, wrapping each function
into decorator

Each decorator represents some type user's message (text, command, file...).
If user sends us command, then decorator, responsible for that command, will
call its function, in which we placed our logic for that command (or text)

Next file is Text_Response.py. It simply has an abstract class MessageResponse,
which should be used as a base class for its inheritors. Each inheritor should
make different type of response, required for a specific command.

I used ABS library to prevent creating instances af the base MessageResponse
class, and to show intention of the developer (me) to make inheritors from
that class, rather than instantiating.

## Good example

```python
@bot.message_handler(commands=['time', 'joke'])
def send_tj_response(message: telebot.types.Message):
    """Response to, you guessed it, 'time' and 'joke' commands"""

    if message.text == '/time':
        responder = TimeResponse(message, bot)
    else:
        responder = JokeResponse(message, bot)

    responder.response()
```

So, when Telebot_Main_Engine catches '/time' or '/joke' command, it calls for function
send_tj_response(message). This function opens up users message and checks for text
inside. Depending on that text it's creating TimeResponse or JokeResponse instance,
packing it into variable responder and simply calls method responder.response().

As you can see, it does not matter, which class would be created. Each of them has
the same method with same signatures, so later we're simply treating it as a variable,
without even knowing and caring about what's inside.

```python
# Base class looks like this:
class MessageResponse(ABC):
    """Abstract class for message response"""

    @abstractmethod
    def __init__(self, message: telebot.types.Message, bot: TeleBot):
        self.message = message
        self.bot = bot

    def response(self):
        pass

# overriding with this:
class JokeResponse(MessageResponse):
    """Responses with a randomly selected joke"""

    def __init__(self, message: telebot.types.Message, bot: TeleBot):
        super().__init__(message, bot)
        self.jokes = ...

    def response(self):
        joke = random.choice(self.jokes)
        self.bot.send_message(self.message.from_user.id, joke)

# and this:
class TimeResponse(MessageResponse):
    """Responses with current time"""

    def __init__(self, message: telebot.types.Message, bot: TeleBot):
        super().__init__(message, bot)

    def response(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        text = f'Current Bot Time = {current_time}'
        self.bot.send_message(self.message.from_user.id, text)
```



## Bad example

```python
class SimpleResponse(MessageResponse):
    """Responses to regular message from user (message without any commands)"""

    def __init__(self, message: telebot.types.Message, bot: TeleBot):
        super().__init__(message, bot)

    # This is an example of violation of LSP
    def response(self, username: str):
        self.bot.send_message(self.message.from_user.id, f'Some response to your text, {username},'
                                                         f' made with neural network')
```

Then there is send_text(message) function, which makes kinda the same and uses class
SimpleResponse, which also overloads base class MessageResponse. But when SimpleResponse
overloads method response, it's also changing signature of base method (which IDE does
not enjoy).

As the result – we still have a working code, even with some extra functionality
because override method now can accept username and add it into response text.
But if. for some reason, we would like not to violate LSP, than we could simply
add another method into inherited class, and that's it.