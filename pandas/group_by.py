import pandas as pd
data = pd.read_excel("D:/gaurav/python note/Expense.xlsx")
print(data)
gp = data.groupby(["Category","Amount"]).agg({"Payment Mode":"count"})
print(gp)