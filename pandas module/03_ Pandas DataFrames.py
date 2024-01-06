'''A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns'''
 
import pandas as pd 
 
data_={"1_name":"vasanth",
      "2_name":"ranjith",
      "3_name":"ragu"}

data_frm=pd.Series(data_)
print(data_frm)

# DataFrame
data_frame={
    "data_1":["1_name","2_name","3_name"],
    "data_2":["vasanth","ranjith","vicky"]
}
df=pd.DataFrame(data_frame)
print(df)

#Locate Row

'''As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)'''

print("locate the row:\n",df.loc[0])

#use a list of indexes:

print("use the list of the ndex:\n",df.loc[[0, 1]])


