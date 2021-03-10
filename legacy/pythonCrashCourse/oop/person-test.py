string = "base16"

fixnum = 0
_float = 0.00
array = list()
array = ['chris', 85]
_hash = {"test": "test"}


# This is a comment
class Person(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "hello"


person1 = Person(name="chris")
print(person1.greet())
