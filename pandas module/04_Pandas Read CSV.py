''' A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'.'''

import pandas as pd

df = pd.read_csv('data.csv')

print(df)
print()
#string formet
print(df.to_string())

#max_rows
'''
The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the pd.options.display.max_rows statement.

In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

You can change the maximum rows number with the same statement.'''

print("max_rows_1:",pd.options.display.max_rows)

pd.options.display.max_rows = 9999

print("max_row_2:",pd.options.display.max_rows)
