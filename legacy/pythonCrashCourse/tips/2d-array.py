N = 10

# This will NOT work because the list is pass by reference. Each element will
# refer to the same list.

matrix = [[0 for i in range(0, N)] * N]

# This is how you can initialize a 2D array.
matrix = [[0 for i in range(0, N)] for j in range(0, N)]

a = [[]] * 3
a[0].append("value")
print(a)
b = [[] for _ in range(3)]
b[0].append("value")
print(b)
