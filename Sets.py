#Creating a set
a={"apple","Grapes","Mango"}
print(a)
x={"apple","Grapes","apple","Mango",True,False} #duplicate values not allowed 
print(x)
y={"Dinesh",21,"Btech",2} #mixed data types
print(y)
print(type(y))

#Accessing set items
print("apple" in a)
print("apple" not in a)

#Adding elements 
a.add("pineapple")
print(a)
a.update(y)
print(a)

#Removing elements 
a.remove("Grapes")
print(a)
x.discard("Mango")
print(x)
x.pop() #remobes random element
print(x)

#loop sets
for x in a:
print(x)

#joining sets
z=a.union(y) #union
print(z)
c=a|y
print(c)
#intersection
d=a.intersection(x) # we can also use & symbol
print(d)


