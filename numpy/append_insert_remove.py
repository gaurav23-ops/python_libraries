import numpy as np

# ------------------------------
# 1. ADDING ELEMENTS (np.append / np.concatenate)
# ------------------------------
arr = np.array([1, 2, 3])

# Example 1: Append single element
print(np.append(arr, 4))  
# [1 2 3 4]

# Example 2: Append multiple elements
print(np.append(arr, [5, 6]))  
# [1 2 3 5 6]

# Example 3: Concatenate two arrays
b = np.array([7, 8, 9])
print(np.concatenate((arr, b)))  
# [1 2 3 7 8 9]

# Example 4: Append along axis (2D array, row-wise)
arr2D = np.array([[1, 2], [3, 4]])
print(np.append(arr2D, [[5, 6]], axis=0))  
# [[1 2]
#  [3 4]
#  [5 6]]

# Example 5: Append along axis (2D array, column-wise)
print(np.append(arr2D, [[7], [8]], axis=1))  
# [[1 2 7]
#  [3 4 8]]


# ------------------------------
# 2. INSERTING ELEMENTS (np.insert)
# ------------------------------
arr = np.array([10, 20, 30, 40])

# Example 1: Insert at beginning
print(np.insert(arr, 0, 5))  
# [ 5 10 20 30 40]

# Example 2: Insert at specific index
print(np.insert(arr, 2, 25))  
# [10 20 25 30 40]

# Example 3: Insert multiple values
print(np.insert(arr, [1, 3], [15, 35]))  
# [10 15 20 30 35 40]

# Example 4: Insert column in 2D array
arr2D = np.array([[1, 2], [3, 4]])
print(np.insert(arr2D, 1, [9, 9], axis=1))  
# [[1 9 2]
#  [3 9 4]]

# Example 5: Insert row in 2D array
print(np.insert(arr2D, 1, [7, 8], axis=0))  
# [[1 2]
#  [7 8]
#  [3 4]]


# ------------------------------
# 3. REMOVING ELEMENTS (np.delete)
# ------------------------------
arr = np.array([100, 200, 300, 400, 500])

# Example 1: Remove element at index
print(np.delete(arr, 2))  
# [100 200 400 500]

# Example 2: Remove multiple indices
print(np.delete(arr, [1, 3]))  
# [100 300 500]

# Example 3: Remove with slicing
print(np.delete(arr, np.s_[::2]))  
# [200 400]  (removed indices 0,2,4)

# Example 4: Remove column from 2D array
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(np.delete(arr2D, 1, axis=1))  
# [[1 3]
#  [4 6]]

# Example 5: Remove row from 2D array
print(np.delete(arr2D, 0, axis=0))  
# [[4 5 6]]
