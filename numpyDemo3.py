import numpy as np

a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

print(np.matmul(a, b))

# Find the determinant
c = np.identity(3)
print(np.linalg.det(c))

# Statistics
stats = np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats,axis=1))
print(np.max(stats))
print(np.sum(stats, axis=0))
