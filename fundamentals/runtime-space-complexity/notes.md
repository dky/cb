# How to Analyze Algorithms

Say we have a sorted list of integers. I want to know if some target, x is in the list.
- [1,2,3,4,5,6,7,8] look for 3.

Approach 1: Search starting from the front, continue if each number is our target.
- 1, 2, 3...

- [1,2,3,4,5,6,7,8] look for 9
- 1,2,3,4,5,6,7,8 - Nope 9 is not in our list. Return False.

- Approach 2: Binary search - continue cutting the list in half until we find our target.

- [1,2,3,4,5,6,7,8] look for 3.
- 4, 2, 3. Return true

- [1,2,3,4,5,6,7,8] look for 9.
- 4, 6, 7, 8 Return false

1. Approach 1 is faster if the target of the search is at the beginning of the list O(1)
2. Approach 2 is faster if the target is not at the beginning of the list.

How do we formally describe if an algorithm is more efficient in terms of run time or memory.

1. Questions 
- How long will my program take?
- How much memory will I use?

Approximation determined on input size.
1000 customer, a new one each day.
How long my program will run as my customers keep increasing?
This is why it's important to understand algos at tech companies.
