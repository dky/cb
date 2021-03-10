numbers = [-4, 1, 2, 5, -6, 7]

# O(n) constant


def greedy_max_sum(nums):
    largest_2_nums = []
    for num in nums:
        largest_2_nums.append(num)
        largest_2_nums.sort(reverse=True)
        print(largest_2_nums)
        # I'm assuming this is the "window" size
        if len(largest_2_nums) > 2:
            largest_2_nums.pop()
    return largest_2_nums[0] + largest_2_nums[1]


print(greedy_max_sum(numbers))
