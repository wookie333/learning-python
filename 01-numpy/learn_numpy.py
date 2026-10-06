import numpy as np
a = np.array([1, 2, 3, 4])

a = np.array([1, 2, 3, 4], 'str_')
print(a)
comp = np.complex64(a)
print(comp)

try:
    print(np.array([1, 2, 5000, 1000], dtype='int8'))
except OverflowError as e:
    print(e)

compl64 = np.array([1.+0.j, 2.+0.j, 3.+0.j, 4.+0.j], dtype='complex64')
np.complex64(compl64)
print(compl64)

print(np.array( "hello" ))
print(np.array([[1, 2], [3, 4], [5, 6]]), '\n') #3i, 2j

print(np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])[0, 1, 1])