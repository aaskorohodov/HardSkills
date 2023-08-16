import datetime
import random
from abc import ABC, abstractmethod

import telebot.types
from telebot import TeleBot


class MessageResponse(ABC):
    """Abstract class for message response"""

    @abstractmethod
    def __init__(self, message: telebot.types.Message, bot: TeleBot):
        self.message = message
        self.bot = bot

    def response(self):
        pass


class JokeResponse(MessageResponse):
    """Responses with a randomly selected joke"""

    def __init__(self, message: telebot.types.Message, bot: TeleBot):
        super().__init__(message, bot)
        self.jokes = [
            'What can you do if you cannot push your git changes?\n Use the --force, Luke',
            'Relationship status?\n Ill leave the relations to the database.',
            'How did the developer announce their engagement?\n They returned true!',
            'What do you call a busy waiter?\n A server.',
            'I’ve been hearing news about this big boolean. Huge if true.',
            '!false (Its funny cause its true.)',
            'A programmers significant other tells them, "Run to the store and pick up a loaf of bread. '
            'If they have eggs, get a dozen." The programmer comes home with 12 loaves of bread.',
            'As a programmer, sometimes I feel a void. And I know I’ve reached the point of no return',
            'Two sql developers walk into a bar & then walk straight out… Because there were no tables they could join',
            'Karl Marx would really not like Java. He was really more a classless sorta guy.'
        ]

    def response(self):
        joke = random.choice(self.jokes)
        self.bot.send_message(self.message.from_user.id, joke)


class TimeResponse(MessageResponse):
    """Responses with current time"""

    def __init__(self, message: telebot.types.Message, bot: TeleBot):
        super().__init__(message, bot)

    def response(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        text = f'Current Bot Time = {current_time}'
        self.bot.send_message(self.message.from_user.id, text)


class SimpleResponse(MessageResponse):
    """Responses to regular message from user (message without any commands)"""

    def __init__(self, message: telebot.types.Message, bot: TeleBot):
        super().__init__(message, bot)

    # This is an example of violation of LSP
    def response(self, username: str):
        self.bot.send_message(self.message.from_user.id, f'Some response to your text, {username},'
                                                         f' made with neural network')
