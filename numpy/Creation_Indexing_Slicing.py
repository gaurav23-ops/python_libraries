import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70])

print("Array:", arr)              # [10 20 30 40 50]

print("\n--- Indexing Examples ---")
print("1. First element:", arr[0])     # 10
print("2. Last element:", arr[-1])     # 70
print("3. Third element:", arr[2])     # 30
print("4. Index 4 element:", arr[4])   # 50
print("5. Negative index (-3):", arr[-3])  # 50

print("\n--- Slicing Examples ---")
print("1. First 3 elements:", arr[:3])       # [10 20 30]
print("2. From index 2 to 5:", arr[2:6])     # [30 40 50 60]
print("3. Every 2nd element:", arr[::2])     # [10 30 50 70]
print("4. Elements from index 1 to end:", arr[1:])  # [20 30 40 50 60 70]
print("5. Reverse array:", arr[::-1])        # [70 60 50 40 30 20 10]
