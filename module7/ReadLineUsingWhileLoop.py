# read all contents line by line

# open the text file
file = open("readTextFile1.txt")

# read all the contents of the text file line by line
content = file.readline()

# print all the lines of text file
while content!="":
    print(content)
    content = file.readline()

# close the text file
file.close()