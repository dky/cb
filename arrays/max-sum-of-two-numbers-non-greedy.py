numbers = [-4, 1, 2, 5, -6, 7]

# O(n^2) Exponential
# Non greedy solution


def non_greedy_max(nums):
    max_sum = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            max_sum = max(max_sum, nums[i] + nums[j])
    return max_sum


print(non_greedy_max(numbers))
