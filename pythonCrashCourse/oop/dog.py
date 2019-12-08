class Dog:
    # Class attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # Instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Instantiate the Dog object
lucky = Dog("Lucky", 13)
print(lucky.name)
print(lucky.age)

# Call instance methods
print(lucky.description())
print(lucky.speak("Howwww Chirp"))
