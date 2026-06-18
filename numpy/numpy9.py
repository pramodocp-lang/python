import numpy as np

# Random decimal numbers between 0 and 1
print("Random numbers:")
print(np.random.rand(3))

# Random 2x3 matrix
print("\nRandom Matrix:")
print(np.random.rand(2, 3, 4))

np.random.seed(100)

print(np.random.rand(3, 3))
print(np.random.randint(10, 50, size = 5))