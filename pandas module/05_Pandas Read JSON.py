'''Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

In our examples we will be using a JSON file called 'data.json'.'''

import pandas as pd 

df = pd.read_json("data.json")
print(df)

# string formet
print(df.to_string())

#Dictionary as JSON
'''

JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.

'''

data={
    "name":{
        "0":"vasanth",
        "1":"nazrin",
        "2":"anu",
        "3":"hari",
        "4":"ananth"
    },
    "age":{
        "0":18,
        "1":17,
        "2":15,
        "3":18,
        "4":19
    },
    "ID":{
        "0":21422247112,
        "1":21422247113,
        "2":21422247114,
        "3":21422247115,
        "4":21422247116
    },
    "deptment":{
        "0":"b.sc.computer science",
        "1":"ba.tamil",
        "2":"b.com",
        "3":"aeto mobiles",
        "4":"eee"
    }
}

data_dataframe=pd.DataFrame(data)
print("json data_frame:\n",data_dataframe)