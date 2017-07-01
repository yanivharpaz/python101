from pprint import pprint as pp

a=[1,2,3,4,5]
b=[6,7,8,9,11]
c=[1,2,6,8,9]

for x in zip(a,b,c):
    pp(max(x))
    pp(x)


def gen123():
    yield 1
    yield 2
    yield 3

g=gen123()
pp(next(g))
pp(next(g))
pp(next(g))

for v in gen123():
    print(v)

import os
import glob

file_sizes={os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}

pp(file_sizes)

f=[(i*'*')  for i in range(20)]

pp(f)

z = [' '*((30-i)//2) + ('*'*i) for i in range(30) if i%2==1]
pp(z)


country_to_capital={'united kingdom':'london','brazil':'brazilia','maroco':'rabat'}

capital_to_country={capital: country for country , capital in country_to_capital.items()}
pp(capital_to_country)


words=['hi','yaniv','and','limor']
dic={x[0]:x for x in words}
pp(dic)

