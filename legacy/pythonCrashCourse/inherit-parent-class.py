# Parent class


class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # Instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class Beagle(Dog):
    def run(self, speed):
        return "{}, the Beagle, runs {}".format(self.name, speed)


snoopy = Beagle("Snoopy", 8)

# Inherits from Dog Class!
print(snoopy.description())  # Prints "Snoopy is 8 years old"

# But still has it's own function.
print(snoopy.run("fast"))  # Prints "Snoopy, the Beagle, runs fast"
