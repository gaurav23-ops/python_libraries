import statistics as stats
import numpy as np
arr_stat = np.array([1, 2, 3, 4, 5, 6, 7])

print("\n--- Statistical Functions ---")
print("1. Mean:", np.mean(arr_stat))             # 4.0
print("2. Median:", np.median(arr_stat))         # 4.0
print("3. Standard Deviation:", np.std(arr_stat))# 2.0
print("4. Variance:", np.var(arr_stat))          # 4.0
print("5. Percentile 25:", np.percentile(arr_stat, 25))  # 2.5


backed_food= [200,200,300,100,100]
print(np.sort(backed_food))
print(np.mean(backed_food))
print(np.median(backed_food))
print(stats.mode(backed_food))