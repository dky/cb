from stopwatch import Stopwatch
import random


def approach_one(our_list, target):
    for i in range(0, len(our_list)):
        number = our_list[i]
        if number == target:
            return i
    return -1


# Choose a random integer and see how it grows.
if __name__ == "__main__":
    input_sizes = [10000, 20000, 40000, 80000, 160000]
    for input_size in input_sizes:
        timer = Stopwatch()
        # input_list = [i for i in range(0, input_sizes)]
        input_list = range(0, input_size)
        target = random.randint(0, input_size)

        total_operations = approach_one(input_list, target)
        print(input_size, total_operations, timer.elapsed_time())
