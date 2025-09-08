import pandas as pd
data={"months" : ["january","february","march","april"]}
df= pd.DataFrame(data)
print(df)
print("-"*40)
def extract(value):
    return value[0:3]
df["short_month"] = df["months"].map(extract)
print(df)