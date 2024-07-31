#  https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

"""
Given a sorted and rotated array arr[] of n distinct elements, the task is to find the index of given target element in the array. 
If target is not present in the array, return -1.

Example:  

Input  : arr[] = {4, 5, 6, 7, 0, 1, 2}, target = 0
Output : 4
"""

def search(nums, target):
    left, right = 0, len(nums) - 1
    while(left <= right):
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1 
            else:
                left = mid + 1
        else:
            if target > nums[mid+1] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

# Example usage
arr1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(search(arr1, target1))  # Output: 4