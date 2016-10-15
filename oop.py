class Classroom:

    def __init__(self):
        self.pepole=[]

    def add_person(self, person):
        self.pepole.append(person)

    def remove_person(self, person):
        self.pepole.remove(person)

    def greet(self):
        for person in self.pepole:
            person.say_hello()



class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        #pass
        print("hello!", self.name)

room = Classroom()
room.add_person(Person("limor"))
room.add_person(Person("yaniv"))
room.add_person(Person("scott"))

print(len(room.pepole), room.pepole)

room.greet()


#p1 = Person("limor")
#p1.say_hello()

#p2 = Person("yaniv")
#p2.say_hello()


