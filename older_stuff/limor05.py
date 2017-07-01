class B(object):
    def __init__(self, name):
        self.name = name

    def check(self):
        if self.name == 'limor':
            print('goood')
        else:
            print('yaniv king')


b = B('limor')
b.check()

y = B('yaniv')
y.check()


with open('/home/yaniv/limor.txt', 'r') as f:
    f.read()

