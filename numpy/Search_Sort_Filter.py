import numpy  as np
arr_search = np.array([10, 20, 30, 20, 40, 50, 20])

print("\n--- Search ---")
print("1. Where is 20?:", np.where(arr_search == 20))   # (array([1, 3, 6]),)
print("2. Greater than 30:", np.where(arr_search > 30)) # (array([4, 5]),)
print("3. Even numbers:", np.where(arr_search % 2 == 0))# all indices
print("4. Less than 25:", np.where(arr_search < 25))    # (array([0, 1, 3, 6]),)
print("5. Equal to 50:", np.where(arr_search == 50))    # (array([5]),)

arr_sort = np.array([30, 10, 40, 20, 5])
print("\n--- Sort ---")
print("1. Sorted array:", np.sort(arr_sort))         # [ 5 10 20 30 40]
print("2. Sorted in-place:", np.sort(arr_sort)[::-1])# [40 30 20 10  5]
print("3. Argsort:", np.argsort(arr_sort))           # [4 1 3 0 2]
print("4. Sort 2D row-wise:\n", np.sort(np.array([[3,2,1],[6,5,4]])))
# [[1 2 3]
#  [4 5 6]]
print("5. Sort 2D column-wise:\n", np.sort(np.array([[3,2,1],[6,5,4]]), axis=0))
# [[3 2 1]
#  [6 5 4]]

arr_filter = np.array([10, 25, 30, 45, 50, 65])
print("\n--- Filter ---")
print("1. Values > 30:", arr_filter[arr_filter > 30])      # [45 50 65]
print("2. Values < 40:", arr_filter[arr_filter < 40])      # [10 25 30]
print("3. Even values:", arr_filter[arr_filter % 2 == 0])  # [10 30 50]
print("4. Odd values:", arr_filter[arr_filter % 2 == 1])   # [25 45 65]
print("5. Between 20 and 60:", arr_filter[(arr_filter > 20) & (arr_filter < 60)]) # [25 30 45 50]