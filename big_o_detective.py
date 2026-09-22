"""
Part 1 - Classify These Functions

Function A: This is o(1) because it's just retrieving one item from a list.

Function B: This is o(n) because it's going through one loop to find a match.

Function C: This is o(n^2) because it is a loop running within a loop, adding every combo in the j loop first then through each of the indexes from i until every loop within a loop combo is processed.

Function D: This is clearly o(log n) simply because it's in a while loop that divides by 2.

Function E: This one is O(n log n) because it's sorted with sorted() that makes it take o(n log n) time.


Part 2 - Write and Benchmark
"""
import random
import time

# O(n^2) because it loops through the list twice
def count_pairs_quadratic(nums, target):
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                count += 1

    return count


# O(n) because it only has to go through the list once
def count_pairs_linear(nums, target):
    seen = {}
    count = 0

    for num in nums:
        needed_num = target - num

        if needed_num in seen:
            count += seen[needed_num]

        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

    return count


# test both functions with lists of 1000, 5000, and 10000
target = 100
sizes = [1000, 5000, 10000]

for size in sizes:
    # make a list with random numbers from 1-100
    nums = [random.randint(1, 100) for i in range(size)]

    start = time.perf_counter()
    count_pairs_quadratic(nums, target)
    quadratic_time = time.perf_counter() - start

    start = time.perf_counter()
    count_pairs_linear(nums, target)
    linear_time = time.perf_counter() - start

    print(
        f"n={size} | quadratic: {quadratic_time:.4f}s "
        f"| linear: {linear_time:.4f}s"
    )

#the output using the timing pattern (will be diff each time)
"""
n=  1000  |  Nested: 0.0129s  |  Set: 0.0001s
n=  5000  |  Nested: 0.3508s  |  Set: 0.0005s
n= 10000  |  Nested: 1.3104s  |  Set: 0.0008s
"""
