import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("\n--- Combining Arrays ---")
print("Concatenate (np.concatenate):", np.concatenate((arr1, arr2)))  
# [1 2 3 4 5 6]

print("Stacked vertically (np.vstack):\n", np.vstack((arr1, arr2)))  
# [[1 2 3]
#  [4 5 6]]

print("Stacked horizontally (np.hstack):\n", np.hstack((arr1, arr2)))  
# [1 2 3 4 5 6]

arr3 = np.array([10, 20, 30, 40, 50, 60])
print("\n--- Splitting Arrays ---")
print("Split into 3 parts (np.split):", np.split(arr3, 3))  
# [array([10, 20]) array([30, 40]) array([50, 60])]