from stopwatch import Stopwatch

# Linear O(N)
# N Runtime
# 2 2
# 4 4
# 6 6


def linear_run_time(N):
    total_operations = 0
    i = 1
    while i < N:
        total_operations += 1
        i += 1
    return total_operations


if __name__ == "__main__":
    input_sizes = [100, 200, 400, 800, 1600, 3200, 6400]
    for input_size in input_sizes:
        timer = Stopwatch()
        linear_run_time(input_size)
        # Relationship you should see is if you double your input the run time
        # is also doubled.
        print(input_size, timer.elapsed_time())
