# creating a class

class Calculator:

    def addition(self, n1, n2):
        result = n1 + n2
        print("Sum of '", n1, "' and '", n2, "' is : ", result)

    def subtraction(self, n1, n2):
        result = n1 - n2
        print("Difference between '", n1, "' and '", n2, "' is : ", result)

    def multiplication(self, n1, n2):
        result = n1 * n2
        print("Multiplication of '", n1, "' and '", n2, "' is : ", result)

    def dividation(self, n1, n2):
        result = n1 / n2
        print("Dividation of '", n1, "' and '", n2, "' is : ", result)


num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : "))

# creating object of Calculator class
obj = Calculator()

# calling the functions using object of Calculator class
obj.addition(num1, num2)
obj.subtraction(num1, num2)
obj.multiplication(num1, num2)
obj.dividation(num1, num2)