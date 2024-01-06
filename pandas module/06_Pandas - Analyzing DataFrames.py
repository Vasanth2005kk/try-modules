import pandas 

df=pandas.read_csv("data.csv")

'''from front secton to specified'''
print(df.head()) #head function is frist five colums prit it. 

#head function sepific colums 
print(df.head(20))

''' from the back section until specified'''

print(df.tail()) #tail function is back five colums prit it.

#tail function sepific colums 
print(df.tail(15))

#Info About the Data

print("inform:",df.info())