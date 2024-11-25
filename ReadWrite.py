file = open('test.txt')

## read() help to read all the contents from a file
## read n number of charter by passing a parameter

# print(file.read(12))

# print(file.readline()) ## print a text file line by line
# print(file.readline())


## print line by line using readline method
# line = file.readline()
#
# while line != "":
#     print(line)
#     line = file.readline()

for line in file.readline():
    print(line)

file.close()


