# raise exception in Python

orderedItems = 1

# raise Exception if condition not satisfied
if orderedItems == 0:
    raise Exception("There are no items for order : ")

else:
    print("Items are successfully ordered : ")


# raise Exception using "assert"
# assert orderedItems==3

print("Success : ")