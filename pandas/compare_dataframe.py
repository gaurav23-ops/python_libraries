import pandas as pd 
dict = {"fuirt":["mango", "apple","banana","papaya"],
       "price":[150,170,120,35],
       "qauntity":[10,20,10,15]}

df1 = pd.DataFrame(dict)
print(df1)
print()
df2 = df1.copy()
print(df2)
print()
df2.loc[0,"price"]=120
print(df2)
print()
print(df1.compare(df2))