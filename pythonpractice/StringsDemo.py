
str = "ArnabKrMondal.com"
str1 = "Automation"
str3 = "Kr"

##Print any char in string
print(str[1]) ## r

## extraxt substr from a string

print(str[0:5]) ## Arnab

## concatinate a string to another string

print(str + str1)

## Check a string is present in a particular string or not

print(str3 in str) ## True/ False

##spilit string, split string element in a particular way and create a list on that

var = str.split(".")
print(var)
print(var[0])

## trim,  trim remove wide spaces from string

str4 = " great "
print(str4.strip()) ## in python trim is done by keyword strip
print(str4.lstrip())
print(str4.rstrip())




