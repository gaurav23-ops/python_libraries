import matplotlib.pyplot as plt

y= [98,68,75,85,96,89]
x =["part1","part2", "part3" ,"part4","part5", "part6"]
color = [ "black","orange", "red", "blue", "grey" , "yellow"]
edgecolor = ["orange","black" ,"black" ,"black","black","black"]
plt.bar(x , y , color = color, edgecolor= edgecolor )
plt.xlabel("parts of harry potter")
plt.ylabel("popularity")
plt.title("popularity of harry poter parts ")
plt.savefig("bar.png")
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv("D:/gaurav/python note/Student.csv")

# Convert Name column to string type
df["Name"] = df["Name"].astype(str)

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df["Name"], df["Marks"], color='skyblue')
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df= pd.read_excel("C:/Users/User/Fullpython/python_libraries/pandas/Expense.xlsx")
plt.bar(df["Payment Mode"], df["Amount"], color='skyblue')
plt.xlabel("Payment Mode")
plt.ylabel("Amount")
plt.title("payment Mode Bar Chart")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()