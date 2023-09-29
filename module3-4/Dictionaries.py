# Creating a dictionary
my_dict = {'name' : 'Piyush Verma', 'age' : 28, 'city' : 'Noida'}
print(my_dict)

# Accessing values by key
# Output: 'Piyush Verma'
print(my_dict['name'])


# Output: 28
print(my_dict['age'])


# Using get() method to handle missing keys
# Output: 'Noida'
print(my_dict.get('city' , 'New Delhi'))
print(my_dict.get('gender' , 'Gender Not Define in Dictionary'))


# Output: 'Not specified'
print(my_dict.get('gender' , 'Not Specified'))

# Modifying values
my_dict['city'] = 'New Delhi'
print(my_dict)


# Adding new key-value pairs
my_dict['Designation'] = 'Automation Test Engineer'
print(my_dict)


# Removing a key-value pair
del my_dict['city']
print(my_dict)


# Iterating through keys
print()
for key in my_dict:
    print(key , my_dict[key])


