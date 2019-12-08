from stopwatch import Stopwatch

# Exponential: O(2^N)
def expoential_run_time(N):
    if N == 0:
        return 1
    total_operations = 0
    total_operations += expoential_run_time(N-1)
    total_operations += expoential_run_time(N-1)
    return total_operations

if __name__ == "__main__":
    input_sizes = [12, 13, 14, 15, 16, 17]
    for input_size in input_sizes:
        timer = Stopwatch()
        total_operations = expoential_run_time(input_size)
        print(input_size, total_operations, timer.elapsed_time())
