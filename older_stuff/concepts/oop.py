class Classroom:
    def __init__(self):
        self._people = []

    def add_person(self, person):
        self._people.append(person)

    def remove_person(self, person):
        self._people.remove(person)

    def greet(self):
        for person in self._people:
            person.say_hello()


class Person:

    def __init__(self, name):
#        print('started')
        self.name = name

    def say_hello(self):
        print("Hello!", self.name)


def main():

    p1 = Person('Yaniv')
#    p1.say_hello('hi')
    p1.name = 'another'
#    p1.say_hello('hi')

    room = Classroom()
    room.add_person(Person('Yaniv'))
    room.add_person(Person('Limor'))
    room.add_person(Person('Chief'))
    room.greet()

if __name__ == "__main__":
    main()

