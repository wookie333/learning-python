import numpy as np
'''a = np.arange(10)
a.shape = 2, 5
print(a)
b = a.reshape(10)
print(b)
a[0] = -1
a.shape = -1, 5
print(a)
print(a.resize(4, 5), refcheck=False)
'''

'''a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
b = a.T
print(b)'''

x_test = np.arange(32).reshape(8, 2, 2)
print(x_test, '\n')
x_test4 = np.expand_dims(x_test, axis=0)
print(x_test4.shape, '\n')
a = np.append(x_test4, x_test4, axis=0)
print(a.shape, '\n')
b = np.delete(a, 0, axis=0)
print(b.shape, '\n')
new_b = np.expand_dims(x_test4, axis=-1)
print(new_b.shape, '\n')
c = np.squeeze(b, axis=0)
print(c.shape, '\n')