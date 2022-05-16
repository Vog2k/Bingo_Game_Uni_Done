import random

import numpy as numpy

arr = [1, 5, 6, 7,8,90, "programming", 234, 43234]

for i in range(100):
    sampler=random.randint(0, numpy.size(arr)-1)
    if arr[sampler] == 'programming':
        print(arr[sampler])
print("print str{0} and int{1}".format("string", 1))