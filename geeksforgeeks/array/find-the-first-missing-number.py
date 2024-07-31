# Link - https://www.geeksforgeeks.org/find-the-first-missing-number/

"""
Given a sorted array of n distinct integers where each integer is in the range from 0 to m-1 and m > n. 
Find the smallest number that is missing from the array. 

Examples:

Input: {0, 1, 2, 6, 9}, n = 5, m = 10 
Output: 3
"""

def findMissingNumber(arr, n, m):
    if arr[0] != 0:
        return 0
    for i in range(0, n-1, 2):
        if arr[i+1] - arr[i] != 1:
            return i+1

arr = [4, 5, 10, 11]
n = 4
m = 12
missing_number = findMissingNumber(arr, n, m)
print(missing_number)