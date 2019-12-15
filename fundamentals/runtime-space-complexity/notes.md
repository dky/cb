# How to Analyze Algorithms

## Say we have a sorted list of integers. I want to know if some target, x is in the list.

[1,2,3,4,5,6,7,8] look for 3.

## Approach 1: Search starting from the front, continue if each number is our target.

1, 2, 3...  

[1,2,3,4,5,6,7,8] look for 9  
1,2,3,4,5,6,7,8 - Nope 9 is not in our list. Return False.  

## Approach 2: Binary Search - continue cutting the list in half until we find our target.

[1,2,3,4,5,6,7,8] look for 3.  

1. First look in the middle of the list: 4
2. Since 3 is -lt 4 we look at the left half [1,2,3]
3. Now look for half of [1, 2, 3]: 2
4. Is 3 > 2? Look to the right and Return True.

4, 2, 3. Return true

[1,2,3,4,5,6,7,8] look for 9.
4, 6, 7, 8 Return false - This is because there is no way 9 can be in the list.

1. Approach 1 is faster if the target of the search is at the beginning of the list O(1)
2. Approach 2 is faster if the target is not at the beginning of the list.

How do we formally describe if an algorithm is more efficient in terms of run time or memory.

1. Questions 
- How long will my program take?
- How much memory will I use?

Approximation determined on input size.

#General 
- 1000 customer, a new one signs up each day.
- How long my program will run as my customers keep increasing?
- I want to know how long my program will run as my inputs continue to grow in the future.
- This is why it's important to understand algorithms at tech companies.

- 6:29 - Beginning of Common orders of growth.


December 14, 2019 - Start getting lost around 23:07 quickly after summary.
