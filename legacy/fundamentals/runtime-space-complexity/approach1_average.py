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
    num_samples = 100

    for input_size in input_sizes:
        timer = Stopwatch()
        # input_list = [i for i in range(0, input_sizes)]
        input_list = range(0, input_size)
        total_runtime = 0

        for i in range(0, num_samples):
            target = random.randint(0, input_size)
            approach_one(input_list, target)
            total_runtime += timer.elapsed_time()
        print(input_size, timer.elapsed_time())
