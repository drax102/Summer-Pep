import numpy as np
import time

# Legacy random functions
np.random.seed(42)
print(np.random.randint(0, 10))
print(np.random.rand())
print(np.random.choice([1, 2, 3, 4, 5]))
print(np.random.uniform(0, 10))

# Time comparison: List vs NumPy Array
size = 1000000

start = time.time()
list_range = list(range(size))
list_time = time.time() - start

start = time.time()
np_array = np.arange(size)
np_time = time.time() - start

print(f"List time: {list_time:.6f}s")
print(f"NumPy time: {np_time:.6f}s")

# Shuffle
arr = np.arange(10)
np.random.shuffle(arr)
print(arr)

# Random choice with probabilities
arr = np.arange(1, 6)
choice = np.random.choice(arr, 10, p=[0.1, 0.2, 0.3, 0.2, 0.2])
print(choice)

# Uniform vs Normal distribution
uniform = np.random.uniform(0, 10, 1000)
print("Uniform mean:", uniform.mean())

normal = np.random.normal(0, 1, 1000)
print("Normal mean:", normal.mean())

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))

# Determinant
print(np.linalg.det(A))
