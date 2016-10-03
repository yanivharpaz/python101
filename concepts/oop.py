
class Person():

    def __init__(self):
        print('started')
        self.name = 'default'

    def say_hello(self, param):
        print("Hello!", param, self.name)


def main():
    p1 = Person()
    p1.say_hello('hi')


if __name__ == "__main__":
    main()