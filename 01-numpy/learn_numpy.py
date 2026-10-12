import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.hstack([a, b]))
print(np.vstack([a, b])) #dims should be =
new_a = np.fromiter(range(18), dtype='int32')
print(new_a.resize((3, 3, 2)))


aa = np.array([1, 2, 3, 4])
bb = np.array([5, 6, 7, 8])

print(np.column_stack([aa, bb]))
'''print(np.row_stack([aa, bb]))'''

'''mass_a = np.arange(1, 13).resize(3, 3, 2)
mass_b = np.arange(13, 26).resize(3, 3, 2)

c0 = np.concatenate([mass_a, mass_b], axis=0)
c1 = np.concatenate([mass_a, mass_b], axis=1)
c2 = np.concatenate([mass_a, mass_b], axis=2)
print(c0.shape)'''

print(np.r_[ np.array([1, 2, 3]), np.array([4, 5, 6])])
print(np.c_[ np.array([1, 2, 3]), np.array([4, 5, 6])])
print(np.hsplit(a, 2))
print(np.vsplit(a, 2))
print(np.array_split(a, 2))