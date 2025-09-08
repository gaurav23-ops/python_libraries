import pandas as pd
data = {"Emp_id":["E01","E02","E03","E04","E05"],
        "Name":["Gaurav","Sham","Sumit","Sandesh","pawan"],
        "Age":[15,20,26,20,25]}

data1 = {"Emp_id":["E01","E02","E03","E04","E05"],
        "Salary":[15000,20000,26000,20000,25000]}
df1= pd.DataFrame(data)
df2 = pd.DataFrame(data1)
print(df1)
print()
print(df2)

print(pd.merge(df1,df2,on = "Emp_id"))
