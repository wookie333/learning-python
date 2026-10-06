import numpy as np
#1
a = np.array([10, 20, 30, 40, 50])
print(a[0])
print(a[-1])
print(a[::2], '\n')

#2
our_massiv = np.array([1, -2, 3, -4, 5])
for x in our_massiv:
    if x > 0:
        print(x)
'''We also have a second way'''
our_massiv = np.array([1, -2, 3, -4, 5])
print(our_massiv[our_massiv > 0], '\n')

#3
new_massiv = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(new_massiv.reshape(3, 4))