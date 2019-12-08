from stopwatch import Stopwatch
# now matter how large n gets the runtime of our algorithm is constant.

def constant_run_time(N):
    total_sum = 0
    for i in range(0, 50):
        total_sum += i
    return total_sum

if __name__ == "__main__":
    input_sizes = [100, 200, 400, 800, 1600, 3200, 6400]
    for input_size in input_sizes:
        timer = Stopwatch()
        constant_run_time(input_size)
        print(input_size, timer.elapsed_time())
