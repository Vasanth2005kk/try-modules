import collections

print(dir(collections))
print(len(dir(collections)))

print(collections.__all__)
va=collections.__all__
print(len(va))
#Counter
name="vasanth","vasanth","ragu","siva","hari","siva","siva"
print(collections.Counter(name))

print(collections.Counter(['B','B','A','B','C','A','B','B','A','C']))
print(collections.Counter(a=9,b=1,c=18))

a=collections.Counter()
a.update([1,1,1,1,1,1,1,1,1,1,1,1,1,4,5,6])
print(a)
my_counter =collections.Counter('abracadabra')
print(my_counter.keys())
print(my_counter.values())
print(my_counter.items())

#OrderedDict
a={}
a["a"]=1
a["b"]=2
print("b:",a)
b=collections.OrderedDict()
b["a"]=1
b["b"]=2
print("B:",b)

#defaultdict
a=collections.defaultdict(list)
for i in range(10,1,-1):
    a[i].append(1)
print(a)
for j,k in a.items():
    print(j,":",k)

#chainMap
c1=["vasanth","v"]
c2=["siva","s"]
c3=["ragu","r"]
a=collections.ChainMap(c1,c2,c3)
print(a)

#nametuple
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])
S =Student('vasanth','10','05.03.2005')
print("The Student age using index is : ",end="")
print(S.name)

#deque
m=[1,4,2,3]
m.append(5)
print(m)
s=collections.deque(m)
s.appendleft(10)
print(s)

