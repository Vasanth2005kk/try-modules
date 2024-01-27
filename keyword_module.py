import keyword

#all function in keyword 
print(dir(keyword))

# all keywords
print("all keywords:",keyword.kwlist)

#soft keywords
print("softkeywords:",keyword.softkwlist)

# check the keywords in boolen formet
print("this s keyword:",keyword.iskeyword("is"))
print("this s not keyword:",keyword.iskeyword("vasanth"))

# check the soft keywords in boolen formet
print("this s soft keyword:",keyword.issoftkeyword("_"))
print("this s not soft keyword:",keyword.issoftkeyword("is"))
