random_list = [5, 1, 3, 4, 2]

# Why are there multiple sorting methods?
# `sorted` returns a new list.
sorted_list = sorted(random_list)
reverse_list = sorted(random_list, reverse=True)

# Calling .sort() modifies the list.
random_list.sort()
print(random_list)

my_new_list = random_list.sort()
print(my_new_list)


# One can also sort lists with a custom key using lambda.
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

        # Provides a string representation of this object.
    def __repr__(self):
        return repr((self.name, self.age))


bob = Person("Bob", 14)
sam = Person("Sam", 12)
ann = Person("Ann", 16)

people = [bob, sam, ann]
# Sort it by their first name.
print(people.sort(key=lambda x: x.name))
print(people.sort(key=lambda x: x.age))
