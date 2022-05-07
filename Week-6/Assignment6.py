#  Sum
# Given an array S of n integers, find three integers in S such that the sum is closest to agiven number, target.
# Return the sum of the three integers.Assume that there will only be one 
# solutionExample: given array S = {-1 2 1 -4}, and target = 1. 
# The sum that is closest to thetarget is 2. (-1 + 2 + 1 = 2)

import math
def findingSum(arr,target):
    closest = math.inf
    sum = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                sum = arr[i]+arr[j]+arr[k]
                if (sum-target)<closest and (sum-target)>=0:
                    closest = sum
    
    return closest


S = [-1, 2, 1, -4]

print(findingSum(S,1))