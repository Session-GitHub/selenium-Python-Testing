# read all content line by line

# open the text file
file = open("readTextFile.txt")

# read the contents of the text file line by line
content = file.readline()
content1 = file.readline()
content2 = file.readline()

# print the content of text file line by line
print(content)
print(content1)
print(content2)


# close the file
file.close()