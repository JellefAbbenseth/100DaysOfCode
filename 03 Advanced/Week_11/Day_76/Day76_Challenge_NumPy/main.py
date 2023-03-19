import numpy as np

import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image

# Understanding NumPy's ndarray

my_array = np.array([1.1, 9.2, 8.1, 4.7])
print(my_array.shape)
print(my_array[2])
print(my_array.ndim)

array_2d = np.array([[1, 2, 3, 9],
                     [5, 6, 7, 8]])
print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)
print(array_2d[1, 2])
print(array_2d[0, :])

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])
print(f'mystery_array has {mystery_array.ndim} dimensions')
print(f'Its shape is {mystery_array.shape}')
print(mystery_array[2][1][-1])
print(mystery_array[2, 1, :])
print(mystery_array[:, :, 0])

# NumPy Mini-Challenges

a = np.arange(10, 30)
print(a)

b = a[-3:]
print(b)
c = a[3:6]
print(c)
d = a[12:]
print(d)
e = a[::2]
print(e)

rev_a = a[::-1]  # np.flip(a)
print(rev_a)

b = np.array([6, 0, 9, 0, 0, 5, 0])
nz_indices = np.nonzero(b)
print(nz_indices)

random_array = np.random.rand(3, 3, 3)
print(random_array)

x = np.linspace(0, 100, num=9)
print(x)

y = np.linspace(-3, 3, num=9)
print(y)

plt.figure(figsize=(10, 6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('X', fontsize=14)
plt.ylabel('Y', fontsize=14)
plt.ylim(-4, 4)
plt.plot(x, y)
plt.show()

noise = np.random.rand(128, 128, 3)
print(noise)
plt.imshow(noise)
plt.show()
