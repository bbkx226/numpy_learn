import numpy as np

a= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

# All 0s matrix
print(np.zeros((2,3)))

# All 1s matrix
print(np.ones((4,2,2), dtype='int32'))

# Any other number
print(np.full((2,2), 99))

# Any other number (full_like)
print(np.full_like(a, 4))
print(np.full(a.shape, 4))

# Random decimal numbers
print(np.random.rand(4,2))
print(np.random.random_sample(a.shape))

# Random Integer values
print(np.random.randint(7, size=(3,3)))

# The identity matrix
print(np.identity(5))

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)

output = np.ones((5,5))

z = np.zeros((3,3))
z[1,1] = 9

output[1:4, 1:4] = z
print(output)
