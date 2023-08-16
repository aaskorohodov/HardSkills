class Test:
    def asd(self):
        print('asdasd')


ttt = Test()

if hasattr(ttt, 'asd'):
    ddd = getattr(ttt, 'asd')
    ddd()