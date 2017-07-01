<<<<<<< Updated upstream


my_value = 15

my_switch = {
    10: 'picked 10',
    20: 'picked 20',
    30: 'picked 30'
}

print(my_value)
print(my_switch)

print(my_switch.get(my_value, 'picked default'))

print(my_switch.get(10,'limor'))
=======
from pprint import pprint as pp
import sys
from itertools import chain

a = [x for x in range(20)]
b = [x for x in range(40,60)]
c = [x for x in range(70,90)]
pp(a)
pp(b)

for kuku in zip(a, b, c):
    print(kuku)
    print(min(kuku))
    print(max(kuku))

z = chain(a, b, c)
pp(z)
print(z)

sys.exit()


my_list = [
    (' ' * ((30 - i) // 2))  # spaces
    + ('*' * i)              # *
    for i in range(30) if i % 2 == 1
    ]
pp(my_list)

my_list = []
for i in range(1, 30, 2):
    item = ' ' * ((30 - i) // 2)
    item += '*' * i
    my_list.append(item)

pp(my_list)

text = '''
In Section 1.1, I look at some programming techniques that flow
  out of the Python language itself, but that are usually not
  obvious to Python beginners--and are sometimes not obvious even
  to intermediate Python programmers. The programming techniques
  that are discussed are ones that tend to be applicable to text
  processing contexts--other programming tasks are likely to have
  their own tricks and idioms that are not explicitly documented in
  this book.
  '''
words = text.split()
word_list = [len(word) for word in words]
pp(word_list)
>>>>>>> Stashed changes
