import numpy as np

arr_agg = np.array([1, 2, 3, 4, 5])

print("\n--- Aggregating Functions ---")
print("1. Sum:", np.sum(arr_agg))                 # 15
print("2. Product:", np.prod(arr_agg))            # 120
print("3. Minimum:", np.min(arr_agg))             # 1
print("4. Maximum:", np.max(arr_agg))             # 5
print("5. Cumulative Sum:", np.cumsum(arr_agg))   # [ 1  3  6 10 15]


a = [100,150,120,130,120,155,111]
b = [10,20,10,20,10,20,1]
price = np.array(a)
quantity = np.array(b)
print("price : ",price , "\n" ,"quantity :", quantity)
print("price max= ",np.max(price))
print(np.sum([price , quantity] , axis = 1))
print(np.cumprod([price , quantity] , axis = 0))

print("Total price= ",np.sum(price))
print("Total quantity= ",np.sum(quantity))