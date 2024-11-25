
# ItemsCart = 0
#2 items will be cart
# if ItemsCart != 2:
    ##raise Exception("Products cart count not match")
## Exception keyword throe some wrong information
#     pass
#
# assert(ItemsCart == 2)

## try catch mechanism

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except Exception as e:
    # print("some how i reached this block because it is failuer")
     print(e)
finally:
    print("cleanning up resources")




