# read all contents line by line

# open the text file
file = open("readTextFile1.txt")

# read all the contents of the text file line by line
content = file.readlines()

# print all the contents of text file line by line
for line in content:
    print(line)


# close the text file
file.close()