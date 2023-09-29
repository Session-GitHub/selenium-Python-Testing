# understanding inheritance in Python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# creating instances of the derived class(Animal)
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method of the Derived classes
print(dog.speak())
print(cat.speak())