import pandas as pd
import numpy as np

data = pd.read_csv("D:/gaurav/python note/Student.csv")
print(data)

print(np.mean(data["Marks"]))
data["Marks"] = data["Marks"].replace(np.nan , 86.42)
print(data)

print("-"*40)

data["Age"] = data["Age"].replace(np.nan , 24)
data.loc [(data["Marks"]<=85,"grade")]="A"
data.loc [(data["Marks"]>85,"grade")]="A+"
print(data)


