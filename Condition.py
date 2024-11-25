
# greeting = "Good Morning"
# if greeting == "Good Morning":
#     print("Condition matches")
# else:
#     print("Condition do not match")
# print("If else is complete")


# age = int(input("enter your age"))
# if age>= 60 & age <= 18:
#     print("can not Drive")
# else:
#     print("Can Drive")
#
# How for loop works in Python

obj = [2, 3, 5, 7, 9]
#for loop helps us to iterate each and every element in the list like other language

for i in obj:
    print(i)

##sum of natural number 1 to 5
sum = 0
for j in range(1,6):## range(i,j) means it can iterate between i, j-1
    sum = sum + j
print(sum)

print("++++++++++++++")
for k in range(1,11,2):##3rd variable in range function in for how many increment after each iteration
    print(k)

## if we do n ot give 1st index in range function then by default it take 0 as 1st index
print("******skipping 1st index*******")
for m in range(10):
    print(m)

#while loop (while loop 1st use to check a condition and the loop is run as much time the condition is true)
num = 1
while num < 20:
    print("Number is:",num)
    num = num + 1
print("while loop execution is done")
##########
numb = 1
while numb<20:
    if numb>10:
        print(numb)
    numb = numb + 1
print("while loop execution is done")
############
## break statement break the loop immediate when it hit the condition
 