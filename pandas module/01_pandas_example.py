import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar) 

print("pandas version:",pd.__version__)

print(dir(pd))
print(len(dir(pd)))