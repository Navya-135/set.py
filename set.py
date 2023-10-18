#set Datatype

#Implicit

#syntax:variableName={item1,item2,....}

a={"apple","grapes","Strawberry"}
print(a)
print(type(a))

#Explicit

#syntax:variableName=set((item1,item2))

a=set(("apple","grapes","Strawberry"))
print(type(a))

#datatype/variable Annotation

#syntax:variableName:set={item1,item2,...}

a:set={"apple","grapes","Strawberry"}
print(type(a))


#CRUD operations

#Create
#add

#syntax:variableName.add(item)

a:set={"apple","grapes","Strawberry"}
print(a.add("Kiwi"))
print(a)

#update

#syntax:variable.update(set variable)

a:set={"apple","grapes","Strawberry"}
b:set={"Car","Bus","Bike"}
a.update(b)
print(a)

#delete

#remove

#syntax:variable.remove(item)

a:set={"1","2","3","4"}
a.remove("3")
print(a)

"""a:set={"1","2","3","4"}
a.remove("5")
print(a)
"""

#discard

#syntax:variable.discard(item)

a:set={"1","2","3","4"}
a.discard("5")
print(a)

#pop

#syntax:variable.pop()

a:set={"1","2","3","4"}
a.pop()
print(a)

#other methods:

#union

#syntax:variable.union(variable)

a={1,2,3,4}
b={5,2,7,8}
print(a.union(b))

#intersection

#Syntax:variable.intersection(variable)

a={1,2,3,4}
b={5,2,7,8}
print(a.intersection(b))






#syntax: