# //Maximum sum contiguous subarray.
# // WEEK 6 : ~8 hrsProblem 6.1: Max Sum Contiguous SubarrayFind the contiguous subarray within an array, 
# // A of length N which has the largest sum.Input Format:The first and the only argument contains an integer array, A. 

# // Output Format: Return aninteger representing the maximum possible sum of the contiguous subarray.

# // Constraints: 1 <= N <= 1e6 -1000 <= A[i] <= 1000 For example:

# // Input 1: A = [1, 2, 3, 4, -10]
# // Output 1: 10
# // Explanation 1: The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

# // Input 2: A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
# // Output 2: 6
# // Explanation 2: The subarray [4,-1,2,1] has the maximum possible sum of 6.

import math

def Kadanes(arr):
    max_sum = -math.inf 
    max_till_now = 0
    for i in arr:
        max_till_now += i
        if max_sum < max_till_now:
            max_sum = max_till_now
        if max_till_now < 0:
            max_till_now = 0

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
arr1 = [1, 2, 3, 4, -10]
print(Kadanes(arr))    # output is 6
print(Kadanes(arr1))    # output is 10
