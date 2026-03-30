#tupels
t = (10, 20, 30, 40)
print("Tuple:", t)
#Accessing elements 
print("First element:", t[0])
print("Last element:", t[-1])
#slicing
print("Sliced tuple:", t[1:4])
#Length of a tuple
print("Length of tuple:", len(t))
#concatenation
t1 = (50, 60)
t2 = t + t1
print("Concatenated tuple:", t2)
#repetition
print("Repeated tuple:", t * 3)
#unpacking
a,b,c,d = t
print(a,b,c,d)
#Indexing
print("Index of 30:", t.index(30))
