# creating a class

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating instances using the Constructor
person1 = Person("Piyush Verma", 28)
person2 = Person("Neeraj Agarwal", 30)

print("First Person's Name is : ", person1.name, "and Age is : ", person1.age)
print("Second Person's Name is : ", person2.name, "and Age is : ", person2.age)
