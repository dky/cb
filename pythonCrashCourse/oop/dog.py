class Dog:
    # Class attribute
    # I'm guessing this is like aglobal var of sorts.
    species = 'mammal'

    # Initializer / Instance Attributes
    # Instance methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # Instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def action(self, action):
        return "{} Performing action {}".format(self.name, action)


# Instantiate the Dog object
lucky = Dog("Lucky", 13)
print(lucky.name)
print(lucky.age)

# Call instance methods
print(lucky.description())
print(lucky.speak("Moo Mooo"))
print(lucky.action("sit"))
