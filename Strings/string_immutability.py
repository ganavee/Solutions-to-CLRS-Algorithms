#Same objects have same id 
s = "Ganavi"
p = "Ganavi"
q = "Jayaram"
print("id of s = {0} id of p = {1} id of q = {2}".format(id(s), id(p), id(q)))


#To create different objects with same value
a = "Ganavi"
b = a.encode().decode()
print("id of a = {0} id of b = {1}".format(id(a), id(b)))

if(a is b):
    print("a and b are Same objects")
else:
    print("a and b are Different objects")

if(a == b):
    print("a and b have Same values")
else:
    print("a and b have Different values")

#Strings immutablity

#Here different objects called Ganavi and Hello are created. so we are not changing any string
c = "Ganavi"
d = c
print("Before modification id of c = {0} id of d = {1}".format(id(c), id(d)))
d = "Hello"
print("After modification id of c = {0} id of d = {1}".format(id(c), id(d)))
print("d = ", d)

'''
#Strings are immutable. Here we are changing the strings itself and hence not possible
e = "Ganavi"
e[0] = 'F'
print(e)
'''
