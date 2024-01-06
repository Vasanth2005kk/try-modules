import pandas as pd

#Replacing Values

df=pd.read_csv("data_1.csv")
df.loc[7,'Duration']=100000000000
print(df.to_string())


for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120 
    print(df.to_string())
print("<------------------->")
#Removing Rows
for x in df.index:
  if df.loc[x, "Duration"] > 110:
    df.drop(x, inplace = True) 
    print(df.to_string())
