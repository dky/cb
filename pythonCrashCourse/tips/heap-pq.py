import heapq
heap = []
# This heapq.heappush(item) ensures that heap[0] is the SMALLEST element.
# heappush() takes 0(log n) time.
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)

# heappop() takes 0(log n) time.
min_element = heapq.heappop(heap)
print(min_element)
min_element = heapq.heappop(heap)
print(min_element)
min_element = heapq.heappop(heap)
print(min_element)

# print(heap)
heap = []
heapq.heappush(heap, (5, 'write code'))
heapq.heappush(heap, (7, 'release product'))
heapq.heappush(heap, (1, 'write spec'))
heapq.heappush(heap, (3, 'create test'))
heapq.heappop(heap)

# Alternatively, say you have a class and you want to add them to a heqpq. You
# will need to implement a '__lt__' (les than) comparator method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Compare by name first, then by age if there's a tie.
        def __lt__(self, other):
            if self.name == other.name:
                return self.age < other.age
            return self.name < other.name

heap = []
heapq.heappush(heap, Person("Ann", '16'))
heapq.heappush(heap, Person("Bob", 14))
heapq.heappush(heap, Person("Sam", 12))
heapq.heappop(heap)
