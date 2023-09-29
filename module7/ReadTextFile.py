# Read all the content using read() method

# open the text file
file = open("readTextFile.txt")

# read all the contents of the text file
# content = file.read()
content = file.read(30)

# print the content of text file
print(content)

# close the text file
file.close()
