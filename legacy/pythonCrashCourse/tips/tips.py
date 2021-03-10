# Basic Functionality
list = []  # Initializes empty list
list.append(1)

print(list)

for i in range(0, 6):
    print(i)
    list.append(i)  # Each append takes O(1) time. Just like a stack.

print(list)
print(len(list))

# You can pop from the end of the list in O(1) time.
last_element = list.pop()

print(last_element)
print(list)  # Notice the last element in the list is now gone...

# Popping from the front of the list
first_element = list.pop(0)
print(first_element)

print(list)

# Constant time index accesses, this is because you are printing out the exact
# memory location
print(list[2])

# Check if an element is in a list, but this will take O(n) time.
print(3 in list)
print(200 in list)

# Iterate through list
total_sum = 0
for num in list:
    total_sum += num
    print(total_sum)

# One can create a new list using an existing list with what we call List
# Comprehension
# I need to read more into this...
string_numbers = [str(x) for x in list]
print(string_numbers)

even_numbers = [x for x in list if (x % 2) == 0]
print(even_numbers)
