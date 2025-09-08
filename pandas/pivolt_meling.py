import pandas as pd

dict= {"keys":["k1","k2","k1","k2"],
      "name":["john","david","ben","mohit"],
      "houses":["red","blue","gren","red"]}
df = pd.DataFrame(dict)
print(dict)
print(df.pivot("keys","name","houses"))