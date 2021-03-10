from stopwatch import Stopwatch

# Logarithmic O(log n)


def log_run_time(N):
    i = 1
    total_operations = 0
    while i < N:
        total_operations += 1
        i = i * 2
    return total_operations


if __name__ == "__main__":
    input_sizes = [10000, 20000, 40000, 80000, 160000, 320000, 640000, 1280000]
    for input_size in input_sizes:
        timer = Stopwatch()
        total_operations = log_run_time(input_size)
        # Total operations increases by 1 as we double the input size.
        print(input_size, total_operations, timer.elapsed_time())
