# Creating List
empty_List = []
numbers = [1, 5, 2, 3, 4, 2, 3, 8, 4, 3]
names = ["Piyush Verma", "Neeraj Agarwal", "Archansh Soni", "Preeti", "Sarika Soni", "Yatendra"]
mixed_data_List = [1, 3.14, "Piyush Verma", "A"]


# Accessing List Element
print(empty_List)
print(numbers)
print(names)
print(mixed_data_List)


# Access the first element (indexing starts at 0)
print(names[0])


# Access the last element (indexing starts at nth position)
print(numbers[-1])


# Get elements from index 2 (inclusive) to 5 (exclusive)
sub_Set = names[1:5]
print(sub_Set)


# Add a single element to the end
numbers.append(26)
print(numbers)


# Add multiple elements to the end
#numbers.extend(7, 8, 9)
#print(numbers)


# Insert 10 at index 2
numbers.insert(2 , 10)
print(numbers)


# Remove the first occurrence of value 4
numbers.remove(2)
print(numbers)


# Remove and return the last element
popped_Element = numbers.pop()
print(numbers)


# Get the index of the first occurrence of value 3
index = numbers.index(3)
print(index)


# Count occurrences of value 3 in the list
count = numbers.count(3)
print(count)


# Reverse the order of elements in the list
numbers.reverse()
print(numbers)

names.reverse()
print(names)


# Sort the list in ascending order
numbers.sort()
print(numbers)


# Sort the list in descending
numbers.sort(reverse=True)
print(numbers)


# Concatenate two lists
combined_List = numbers + names
print(combined_List)


# Get the number of elements in the list
size = len(combined_List)
print(size)


# Create a shallow copy of the list
copied_List_Numbers = numbers.copy()
print(copied_List_Numbers)


# Remove all elements from the list
numbers.clear()
print(numbers)


