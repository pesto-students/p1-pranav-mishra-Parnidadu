# Sort array of 0's,1's and 2's
# Given an array of size N containing only 0s, 1s, and 2s; 
# sort the array in ascendingorder. 

# Example 1:Input:N = 5 arr[]= {0 2 1 2 0}
# Output:0 0 1 2 2


def sortArr(arr):
    start = 0
    for i in range(len(arr)):
        if arr[i]==0:
            temp = arr[start]
            arr[start] = arr[i]
            arr[i] = temp
            start+=1
    for i in range(len(arr)):
        if arr[i] == 1:
            temp = arr[start]
            arr[start] = arr[i]
            arr[i] = temp
            start+=1
    for i in range(len(arr)):
        if arr[i] == 2:
            temp = arr[start]
            arr[start] = arr[i]
            arr[i] = temp
            start+=1
    
    return arr

# time Complexity is O(N)
# Space complexity is 1

arr = [0,1,2,0,1,0,1,2,0,1,2,2,1,1]

print(sortArr(arr))
