import matplotlib.pyplot as plt
import numpy as np

x =np.random.randint(1,10,50)
y =np.random.randint(10,100,50)
color = np.random.randint(10,100,50)
plt.scatter(x,y , marker= "*" ,c = color)
plt.show()


import pandas as pd 
 
df = pd.read_csv("D:/gaurav/python note/Student.csv")
df["Name"] = df["Name"].astype(str)

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.scatter(df["Name"], df["Marks"], color='skyblue')
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()