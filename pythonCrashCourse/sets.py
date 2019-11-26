#declare empty set
even_num_set = set()
even_num_set.add(2) #O(1)
even_num_set.add(4) #O(1)

odd_num_set = set()
odd_num_set.add(1) #O(1)
odd_num_set.add(3) #O(1)

print(3 in even_num_set)
print(2 in even_num_set)

# We can do a set union as well in O(m+n) time.
union_num_set = even_num_set.union


