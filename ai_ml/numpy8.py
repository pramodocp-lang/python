import numpy as np

# Random decimal numbers between 0 and 1
print("Random numbers:")
print(np.random.rand(3))

# Random 2x3 matrix
print("\nRandom Matrix:")
print(np.random.rand(2, 3, 4))

np.random.seed(42)

print(np.random.randint(1, 5, size = 5))