from stopwatch import Stopwatch

#Linearithmic: O(N log N)
# This should be much faster than quadratic

def linearithmic_run_time(N):
    i = 1
    total_operations = 0
    while i < N:
        j = 1
        while j < N:
            j = j * 2
            total_operations += 1
        i += 1
    return total_operations


if __name__ == "__main__":
    input_sizes = [10000, 20000, 40000, 80000, 160000, 320000, 640000, 1280000]
    for input_size in input_sizes:
        timer = Stopwatch()
        total_operations = linearithmic_run_time(input_size)
        #Total operations increases by 1 as we double the input size.

        print(input_size, total_operations, timer.elapsed_time())
