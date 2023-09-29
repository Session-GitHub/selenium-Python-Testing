# Try Catch Mechanism in Python

try:
    # open the text file
    file = open("readTextFile1.txt")

    # read all the contents of the text file
    content = file.read()

    # print the content of the text file
    print(content)

    # close the text file
    file.close()

except Exception as e:
    print(e)

print("Try-Except has Success : ")
