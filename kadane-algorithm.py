"""
Kadane's algorithm is a popular algorithm to solve the "Maximum Subarray Problem," which aims to find the contiguous subarray within a one-dimensional numeric array that has the largest sum.

Here's a step-by-step explanation and a simple Python implementation of Kadane's algorithm:

Initialization: Start with two variables:

max_current to keep track of the maximum sum of the subarray ending at the current position.
max_global to keep track of the maximum sum found so far across all subarrays.
Iterate through the array: For each element in the array:

Update max_current to be the maximum of the current element itself or the sum of max_current and the current element.
Update max_global if max_current is greater than max_global.
Result: The value in max_global will be the maximum subarray sum.
"""

def kadane_algorithm(nums):
    # Initialize variables
    max_current = nums[0]
    max_global = nums[0]
    start = end = 0
    temp_start = 0
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
            temp_start = i
        else:
            max_current += nums[i]
        
        if max_current > max_global:
            max_global = max_current
            start = temp_start
            end = i
    
    return max_global, start, end

# Example usage
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start_index, end_index = kadane_algorithm(array)
print(f"The maximum subarray sum is: {max_sum}")
print(f"The subarray starts at index {start_index} and ends at index {end_index}")
print(f"The subarray is: {array[start_index:end_index+1]}")
