import numpy as np
from numpy import array
from time import time


# import timeit
#
# timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# timeit.timeit('"-".join(map(str, range(100)))', number=10000)

# a = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# b = a.reshape(2, 5)
# print(b)


array_2d = np.arange(12, 36).reshape((4, 6))
print(array_2d)

print(array_2d[array_2d % 5 == 1])
