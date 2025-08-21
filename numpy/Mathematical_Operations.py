import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("\n--- Mathematical Operations ---")
# Using operators
print("Addition (a + b):", a + b)           # [11 22 33 44]
print("Subtraction (b - a):", b - a)        # [ 9 18 27 36]
print("Multiplication (a * b):", a * b)     # [ 10  40  90 160]
print("Division (b / a):", b / a)           # [10. 10. 10. 10.]
print("Power (a ** 2):", a ** 2)            # [ 1  4  9 16]

# Using NumPy functions
print("Addition (np.add):", np.add(a, b))       # [11 22 33 44]
print("Subtraction (np.subtract):", np.subtract(b, a))  # [ 9 18 27 36]
print("Multiplication (np.multiply):", np.multiply(a, b)) # [ 10  40  90 160]
print("Division (np.divide):", np.divide(b, a))   # [10. 10. 10. 10.]
print("Power (np.power):", np.power(a, 2))        # [ 1  4  9 16]
