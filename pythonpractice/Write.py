## Read the file and store all the line in list
## reverse thr list
## write the list back to the file
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content) ## to reversed the item present in list
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)




