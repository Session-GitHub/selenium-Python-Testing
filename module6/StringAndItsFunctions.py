text = "selenium Is a Very good PRODUCT"

# upper() function to convert
# string to upper case
print("\n1) Converted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\n2) Converted String:")
print(text.lower())

# converts the first character to
# upper case and rest to lower case
print("\n3) Converted String:")
print(text.title())


# swaps the case of all characters in the string
# upper case character to lowercase and vice versa
print("\n4) Converted String:")
print(text.swapcase())


# convert the first character of a string to uppercase
print("\n5) Converted String:")
print(text.capitalize())


# original string never changes
print("\n6) Converted String:")
print(text)


# strip() function
print("\n7) Converted String:")
print(text.strip())


# replace the text using replace() function
print("\n8) Converted String:")
new_text = text.replace("selenium" , "Selenium-Python")
print(new_text)


# split() function
print("\n9) Converted String:")
print(text.split(" "))


# some another functions are
print("\n10) Converted String:")
string = "Selenium-Python"
print("\n")
print(string[0])
print(string[2:5])
print(string[:4])
print(string[2:])