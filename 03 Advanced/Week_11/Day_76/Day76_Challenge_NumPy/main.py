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

# Linear Algebra with Vectors

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
print(v1 + v2)
print(v1 * v2)

# Python Lists vs ndarrays
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]
print(list1 + list2)
# print(list1 * list2) -> TypeError!

# Broadcasting and Scalars

array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])
print(array_2d + 10)
print(array_2d * 5)

# Matrix Multiplication with @ and .matmul()

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

print(f'{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.')
print(f'{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.')
print('Dimensions of result: (4x2)*(2x3)=(4x3)')

c = np.matmul(a1, b1)
print(c)
print(f'Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.')

# Manipulating Images as ndarrays

img = misc.face()
plt.imshow(img)

print(type(img))
print(img.shape)
print(img.ndim)

grey_vals = np.array([0.2126, 0.7152, 0.0722])

sRGB_array = img / 255
grey_vals = np.array([0.2126, 0.7152, 0.0722])
img_gray = sRGB_array @ grey_vals # img_gray = np.matmul(sRGB_array, grey_vals)
plt.imshow(img_gray, cmap='gray')

print(a1, end="\n\n")
print(np.flip(a1))

plt.imshow(np.flip(img_gray), cmap='gray')
plt.show()
plt.imshow(np.rot90(img))
plt.show()
solar_img = 255 - img
plt.imshow(solar_img)
plt.show()

# Use your Own Image!

file_name = 'yummy_macarons.jpg'

my_img = Image.open(file_name)
img_array = np.array(my_img)
print(img_array.ndim)
print(img_array.shape)

plt.imshow(img_array)
plt.show()
plt.imshow(255-img_array)
plt.show()
