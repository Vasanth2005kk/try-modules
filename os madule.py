import os

#print(dir(os))

print(os.getcwd())
os.chdir("../")

print(os.getcwd())
os.chdir("//home//vasanth2005kk//vs code")

print(os.getcwd())

print(os.listdir())
print(os.listdir("/home/vasanth2005kk/PycharmProjects"))
'''for i in os.listdir():
    print(i)'''
'''os.mkdir("vasanth")
print(os.listdir())
'''

print(os.chdir("/home/vasanth2005kk/PycharmProjects/vglug/file"))
print(len(os.listdir()))
#s.rename("vowels_reading","Vowels_Reading")
print(len(os.listdir()))

path=os.path.exists("/home/vasanth2005kk/github/vasanth")
#print(path)
print(os.path.isdir("/home/vasanth2005kk/PycharmProjects/vglug/file"))

print("<____________________________________>")

#print(os.getcwd())
#print(os.listdir())
print(os.stat("vowels_reading"))
print(os.stat("vowels_reading").st_size)

print(os.system("ls"))

print(os.popen("ls"))
print((os.popen("dir").read()))

'''x=os.walk("/home/vasanth2005kk/vs code")
for i in x:
    print(i)
'''
from os import path

s=os.listdir()
print(s)
print(os.getcwd())
print(path.join("/home/vasanth2005kk/PycharmProjects","naanmuthalaven"))

files=os.listdir()

for i in files:
    fullpath=path.join(os.getcwd(),i)
    print(fullpath)
    print(path.isdir(fullpath))
    print(path.isfile(fullpath))
    print(path.split(fullpath)[1])
    print(path.splitext(fullpath))
