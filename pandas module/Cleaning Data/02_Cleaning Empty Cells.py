import pandas

#Remove Rows
'''dropna function is emt spece is remove function'''

df=pandas.read_csv("data.csv")

new_df=df.dropna()
print(new_df.to_string())

'''If you want to change the original DataFrame, use the inplace = True argument:'''

df.dropna(inplace=True)
print(df.to_string())

#Replace Empty Values

df.fillna(130, inplace = True) 
print(df.to_string())

df["Calories"].fillna(130, inplace = True) 

print(df.to_string())

#Replace Using Mean, Median, or Mode

mean_x=df.mean()
print("mean:\n",mean_x)

mediam_x=df.median()
print("mediam:\n",mediam_x)

mode_x=df.mode()
print("mode:\n",mode_x)

data=[60,'20201207',110,136,374.0]

df_date=pandas.to_datetime(data[1])
print(df_date)