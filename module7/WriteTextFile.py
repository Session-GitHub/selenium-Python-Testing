# writing data into a text file

# the data we want to write in a text file
data = "This is some data to write into the file:"

with open("writeTextFile.txt" , "w") as file:
    file.write(data)
    print("Data has been successfully written :")


# close the text file
file.close()