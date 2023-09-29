# Example for a simple function that calculates the square of a number

num = int(input("Please enter a number : "))


def square(number):
    squared = number ** 2
    return squared


result = square(num)
print("Square of '", num, "' is : ", result)
