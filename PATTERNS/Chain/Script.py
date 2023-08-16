from time import sleep
from HandlersRegistration import HandlerRegistrator


run = True
handler = HandlerRegistrator().make_handler()
print('This is a calculator, enter your expression. It should be simple, dont get too exited!\n'
      'When you get bored, type "exit".')
sleep(1)

while run:
    raw_data = input('Input your expression:\n')
    if raw_data == 'exit':
        run = False
        print('Goodbye')
    else:
        print(handler.handle(raw_data))
