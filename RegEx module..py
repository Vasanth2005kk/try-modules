import re

print(dir(re))
print(len(dir(re)))

print(re.__all__)
print("__all_lenth:",len(re.__all__))

function_example="my name is vasanth"

'''
findall 	Returns a list containing all matches
search 	Returns a Match object if there is a match anywhere in the string
split 	Returns a list where the string has been split at each match
sub 	Replaces one or many matches with a string
'''

# findall() function

print(re.findall("is",function_example))

# search() function

search=re.search("is",function_example)
print(search)
print("strating loction :",search.start())
print("ending loction :",search.end())

# split() function

print(re.split(" ",function_example))

#sub () function

print(re.sub(" ","@",function_example))
print(re.sub(" ","@",function_example,2))

#Metacharacters:
#[] ===> gruop of chracters in the list square bracket example ==> "[a-m]"

text="my name is vasanth"
variable_stord=re.findall("[m-z]",text)
print(variable_stord)
variable_stord_1=re.findall("[mnopqrstuvwxyz]",text)
print(variable_stord_1)


# \ ===> singles a special sequence and this is 10 types
#they are

# \A ==> same as the data is in the list

print("starting the latter is the result:",re.findall("\Amy",text))
print("not starting the latter is the result:",re.findall("\Avasanth",text))

'''\B ===>  	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")
thare are two type:
e.g: the rain in spain
r"\Bain" ==> "ain" is present, but not at the beginning of the words
r"ain\B" ==> "ain" is present, but not at the end of the words
                              or
r"\bin" ==> "ain" is present at the beginning of the words
r"ain\b" ==> "ain" is present at the end of the words
'''
example="the rain in spain"
print(re.findall(r"\Bain",example))
print(re.findall(r"e\B",example))
#                   or
print(re.findall(r"\be",example))
print(re.findall(r"ain\b",example))

#\d ===> this use is the only digit

no_digit_word="i am living in parikkal"
digits="my mark is 63"

print("no digit word:",re.findall("\d",no_digit_word))
print("digit word:",re.findall("\d",digits))

# \D ===> this use the is the all word in list in print it and number not removed

print("no digit word:",re.findall("\D",no_digit_word))
print("digit word:",re.findall("\D",digits))

#\s ===> this use is space print it

print("only for space:",re.findall("\s",no_digit_word))

#\S ===> this use is not space print it

print("without space:",re.findall("\S",no_digit_word))

#\w ==> this in use in a to Z and 0 to 9 and underscore _ character in print

x="this_is spcile charcters =!@#$%^&*()"
print("spcile charcters not print it:",re.findall("\w",x))

#\W ==>only for spcile charcters print it

print("spcile charcters print it:",re.findall("\W",x))

#\Z ==>the end of the word is right in print it

print("right word:",re.findall("spain\Z",example))
print("not right word:",re.findall("the\Z",example))

# . ===> Any character (except newline character)

hello="hellow world!"
print(re.findall("h....w",hello))

# ^ ===> this use is for strating olny chacking

print(re.findall("^hellow",hello))
print(re.findall("^world!",hello))

# $ ==> this use is for ending olny chacking

print(re.findall("hellow$",hello))
print(re.findall("world!$",hello))

# * ===> 	Zero or more occurrences

print(re.findall("h.*ow",hello))

# + ===>  	One or more occurrences

print(re.findall("he.+ow",hello))

# ? ===> 	Zero or one occurrences

print(re.findall("hellow?",hello))

# {} ==>  	Exactly the specified number of occurrences

print(re.findall("he.{3}w",hello))

# | ===>  	Either of one

names="vasanth siva hari"
output=re.findall("ranjith|vasanth",names)

print(output)

