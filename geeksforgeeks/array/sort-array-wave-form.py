# Link - https://www.geeksforgeeks.org/sort-array-wave-form-2/

"""
Sort an array in wave form
Last Updated : 12 Jun, 2024
Given an unsorted array of integers, sort the array into a wave array. An array arr[0..n-1] is sorted in wave form if:
arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

Examples:

Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} 
Explanation: 
here you can see {10, 5, 6, 2, 20, 3, 100, 80} first element is larger than the second and the same thing is repeated again and again. large element – small element-large element -small element and so on .it can be small element-larger element – small element-large element -small element too. all you need to maintain is the up-down fashion which represents a wave. there can be multiple answers.

Input: arr[] = {20, 10, 8, 6, 4, 2}
Output: arr[] = {20, 8, 10, 4, 6, 2}
"""

# A idea is to use sorting. First sort the input array, then swap all adjacent elements.
# Time Complexity: O(N*log(N))
# Auxiliary Space: O(1)

def sortInWave(arr, n):
    
    #sort the array
    arr.sort()
   
    # Swap adjacent elements
    for i in range(0,n-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

# Driver program
arr = [10, 90, 49, 2, 1, 5, 23]
sortInWave(arr, len(arr))
for i in range(0,len(arr)):
    print (arr[i],end=" ")
print()


"""
Wave Array Optimized Approach
The idea is based on the fact that if we make sure that all even positioned (at index 0, 2, 4, ..) elements are greater than their adjacent odd elements, 
we don’t need to worry about oddly positioned elements. 
Follow the steps mentioned below to implement the idea:

Traverse all even positioned elements of the input array, and do the following. 
If the current element is smaller than the previous odd element, swap the previous and current. 
If the current element is smaller than the next odd element, swap next and current.
Time Complexity: O(N)
Auxiliary Space: O(1)
"""

def sortInWaveOptimized(arr, n):

    # Traverse all even elements
    for i in range(0, n - 1, 2):

        # If current even element is smaller than previous
        if (i > 0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]

        # If current even element is smaller than next
        if (i < n-1 and arr[i] < arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]


# Driver program
arr = [10, 90, 49, 2, 1, 5, 23]
sortInWaveOptimized(arr, len(arr))
for i in range(0, len(arr)):
    print(arr[i], end=" ")