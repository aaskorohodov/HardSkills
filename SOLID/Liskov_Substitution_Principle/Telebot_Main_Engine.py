from Text_Response import *
"""To start this bot, you simply need to 'pip install pyTelegramBotAPI' and run this file.

*! This will activate a telegram-bot, with the name 'DY_useless_bot' (this bot is already there, you can find it),
but after running this file, bot will start to response. If this bot have been already started somewhere else,
this will result in conflicts. So, please, make sure to make your own bot, which is costless and takes 1 minute:
1. Find BotFather
2. Ask him for brand new bot with a new name
3. Get token from BotFather and copy-paste it into 'bot = telebot.TeleBot('Token')'
"""


# This is a bot-token. Do not steal it, create your own with BotFather (which is a telegram-bot itself)
bot = telebot.TeleBot('1879041775:AAG14Vz9P4AP4hjOGOOwYKbbFJGFSrWQEgs')


# This decorator caches all messages from user with command '/start'. Command is any message, starts with '/'
@bot.message_handler(commands=['start'])
def send_start_response(message: telebot.types.Message):
    """Response to, you guessed it, 'start' command"""

    text = '/joke\n' \
           '/time'
    bot.send_message(message.from_user.id, text)


@bot.message_handler(commands=['time', 'joke'])
def send_tj_response(message: telebot.types.Message):
    """Response to, you guessed it, 'time' and 'joke' commands"""

    if message.text == '/time':
        responder = TimeResponse(message, bot)
    else:
        responder = JokeResponse(message, bot)

    responder.response()


@bot.message_handler(content_types=['text'])
def send_text(message: telebot.types.Message):
    """If any special logic would be added – will response to text with text"""

    responder = SimpleResponse(message, bot)
    responder.response(message.from_user.username)


bot.infinity_polling()
