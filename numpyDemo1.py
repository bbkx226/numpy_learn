import numpy as np

a= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

# Get a specific element [row, column]
print(a[1, 5])

# Get a specific row
print(a[0, :])

# Get a specific column
print(a[:,2])

# Getting a little more fancy [start_index:end_index:stepsize]
print(a[0, 1:-1:2])

# 3-d example
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)

# Get specific element (work outside in)
print(c[0,1,1])

