import numpy as np

a = np.array([1,2,3],dtype='int32')
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(a)
print(b)

# Get dimension
print(a.ndim)

# Get Shape
print(b.shape)

# Get Type
print(a.dtype)

# Get Size
print(a.itemsize)

#Get total size
print(a.nbytes)
