# Using maps with lamdas
num_list = [0, 1, 2, 3, 4, 5]


# Takes each element of num_list and multiples it by 2 (double)
double_list = map(lambda n: n * 2, num_list)
print(list(double_list))


# filter example
numList = [30, 2, -15, 17, 9, 100]


greater_than_10 = list(filter(lambda n: n > 10, numList))
print(greater_than_10)
