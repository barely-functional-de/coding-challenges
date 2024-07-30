# Link - https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/

"""
Rearrange positive and negative numbers in O(n) time and O(1) extra space
Last Updated : 16 Apr, 2024
An array contains both positive and negative numbers in random order. 
Rearrange the array elements so that positive and negative numbers are placed alternatively. 
A number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. 
If there are more negative numbers, they too appear at the end of the array.

Input: [-1, 3, -2, -4, 7, -5]
Output:[7, -2, 3, -5, -1, -4]
"""

#  Python program to put positive numbers at even indexes (0,  // 2, 4,..) and
#  negative numbers at odd indexes (1, 3, 5, ..)

# The main function that rearranges elements of given array. 
# It puts  positive elements at even indexes (0, 2, ..) and 
# negative numbers at odd indexes (1, 3, ..).
def rearrange(arr, n):
    # The following few lines are similar to partition process
    # of QuickSort.  The idea is to consider 0 as pivot and
    # divide the array around it.
    i = -1
    for j in range(n):
        if (arr[j] < 0):
            i += 1
            # swapping of arr
            arr[i], arr[j] = arr[j], arr[i]

    printArray(arr, n)
    print()
    # Now all positive numbers are at end and negative numbers
    # at the beginning of array. Initialize indexes for starting
    # point of positive and negative numbers to be swapped
    pos, neg = i+1, 0
 
    # Increment the negative index by 2 and positive index by 1,
    # i.e., swap every alternate negative number with next 
    # positive number
    while (pos < n and neg < pos and arr[neg] < 0):

        # swapping of arr
        arr[neg], arr[pos] = arr[pos], arr[neg]
        print()
        printArray(arr, n)
        print()
        pos += 1
        neg += 2

# A utility function to print an array
def printArray(arr, n):
    
    for i in range(n):
        print (arr[i],end=" ")
 
# Driver program to test above functions
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
printArray(arr, len(arr))
print()
n = len(arr)
rearrange(arr, n)
printArray(arr, n)
