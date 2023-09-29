
sentence = str(input("Enter a Line : "))

char_to_count = "e"
count = 0

for char in sentence:
    if char == char_to_count:
        count += 1

print("Occurrences of ", char_to_count, ": ", count)
