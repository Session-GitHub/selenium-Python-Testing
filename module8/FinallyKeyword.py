# Finally Keyword with exceptions in Python

try:
    # open the text file
    file = open("readTextFile.txt")

    # read all the contents of the text file
    content = file.read()

    # print the content
    print(content)

    # close the text file
    file.close()

except Exception as e:
    print(e)

finally:
    print("\n No matter that above is any Exception or not, i will execute surely...")