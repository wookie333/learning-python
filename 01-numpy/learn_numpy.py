import numpy as np

a = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
print(a.dtype)
a.dtype = np.int8()
print(a)
print(a.size)
a.dtype = 'float64'
print(a.itemsize)
b = np.ones((3,4,5))
print(b)
print(b.ndim)
print(b.shape)
c = b.reshape(3, 2, 10)
print(c)
print(b)
b[0, 0] = 10
print(b)
print(c)
print(id(b), id(c))
new_a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
new_b = new_a.view()
new_a.shape = 3, 3
print(new_b)
c = new_a.copy()
new_a[0] = 100
print(a)