'''A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.'''

import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

#index
print("index assin :",myvar[0])

print("<____new Labels create___")
#new Labels create
myvar=pd.Series(a,["a","b","c"]) #this value assin in index lenth equal not this assin error the statment

print(myvar)

# When you have created labels, you can access an item by referring to the label.

print("lable access:",myvar["b"])

#Key/Value Objects as Series

sample=pd.Series({"day1":100,
                  "day2":200,
                  "day3":300})
print(sample)

sample_index=pd.Series(sample,index=["day1","day3"])
print(sample_index)

#DataFrames

data = {
  "names": ["vasanth","hari","ragu"],
  "mark": [50, 40, 45]
}

dataframe = pd.DataFrame(data,["1_name","2_name","3_name"]) 

print(dataframe)