from idna import valid_label_length

value = [1,2,"Arnab",4,5]
## list is a data type that allows multiple values and can be different data types

print(value[2]) #Arnab
print(value[3])#4
print(value[-1])#5 print last item
print(value[1:3])# [2, "Arnab"] extract sub list
value.insert(3, "Kumar") #to insert some value inside a particular position in a list
print(value)

value.append("End")#add a new value at the end of a list
print(value)

value[2] = "ARNAB" #update a element inside list
print(value)
del value[1 ]
print(value)

## main difference between list and tuple is tuple is immutable where list is mutable
## and Tuple is declare using '()' this bracket

TupleVal = (1, 2, "Arnab", 4.5)
print(TupleVal[3])
##TupleVal[3] = 5 ## Type error come because it is not suport any update operation
print(TupleVal)

## Dictionary
## there is no specific rule to define "" to key or value it is based upon in the data type

dic = {1: "Arnab" , "a" : 2, 3: "abc", "d" : "Mondal"}
print(dic)
print(dic["d"]) ## Mondal

## create dictionary dynamically runtime

dict = {}
dict["firstName"] = "Arnab"
dict["LastName"] = "Mondal"
dict["gender"] = "Male"
print(dict)
print(dict["LastName"])

