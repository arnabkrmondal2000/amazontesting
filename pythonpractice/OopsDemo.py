# arr = [0,1,2,3,4,5,6,7123,8,9,10,11]
#
# # In the array given above find the index where the integer is not the same with the array index
#
# def find_mismatch(l):
#     for i in range(len(l)):
#         if l[i] != i:
#             return i
#
# # driver function
# ans = find_mismatch(arr)
# print(ans)
from encodings import search_function


### Classes
## classes are user defined blueprint or prototype
## methods, class variables, instance variable, constructor etc
## objects for your classes
## "class" keyword use to create class in python

# class Calulator:
#     num = 100
#
#     def getData(self):
#         print("I am now executing a method in class")
#
# obj = Calulator() ## to create new object from class we just call the class name their is not any new operator
# print(obj.getData())
# print(obj.num)

## constructor is an a method which automatically called when we create a object from class
## Constructor is just like a method in a class which is called when object is created

## self keyword is mandatory for calling variables named into method
## instance and class variables have whole different perpose
## constructor name should be __init__
class Calulator:
    num = 100 ## class variable
    ##default constractor
    ## constructor syntex is little different
    def __init__(self,a,b):
        self.firstNmber = a
        self.seconNumber = b
        print("I am called automatically when object is created")
    def getData(self):
        print("I am now executing a method in class")
    def Summation(self):
        return self.firstNmber + self.seconNumber



obj = Calulator(4,5) ## to create new object from class we just call the class name their is not any new operator
print(obj.getData())
print(obj.Summation())
# print(obj.num)



