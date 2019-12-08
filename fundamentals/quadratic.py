from stopwatch import Stopwatch

def quadratic_run_time(N):
    i = 1
    total_operations = 0
    while i < N:
        j = 1
        while j < N:
            total_operations += 1
            j += 1
        i += 1
    return total_operations

if __name__ == "__main__":
    # input_sizes = [10000, 20000, 40000, 80000, 160000, 320000, 640000, 1280000]
    # input_sizes take really long to compute, dropping a zero to make this run
    # slightly quicker.
    input_sizes = [1000, 2000, 4000, 8000, 16000]
    for input_size in input_sizes:
        timer = Stopwatch()
        total_operations = quadratic_run_time(input_size)
        print(input_size, total_operations, timer.elapsed_time())
