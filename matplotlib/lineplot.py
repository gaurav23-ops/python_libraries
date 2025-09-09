import matplotlib.pyplot as plt
import pandas as pd
x = ["days1","days2","days3","days4","days5"]
y = [300,450,250,400,200]
y1 =[250,360,200,500,400]
plt.plot(x,y,marker = "o",color = "red",label= "week1")
plt.plot(x,y1,marker = "o" , label= "week1")
plt.legend()
plt.show()

df= pd.read_excel("C:/Users/User/Fullpython/python_libraries/pandas/Expense.xlsx")
grouped_by = df .groupby("Category")["Amount"].sum()
print(grouped_by)
plt.plot(grouped_by.index, grouped_by.values)
# plt.plot(df["Date"], df["Amount"])
print(df)
plt.show()