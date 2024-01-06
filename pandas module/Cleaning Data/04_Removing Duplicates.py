import pandas as pd 

df=pd.read_csv('data_1.csv')

du_df=df.duplicated()
print(du_df)


df.drop_duplicates(inplace = True)

print(df.to_string())

#Notice that row 9 has been removed from the result

