# 6.5: Pair With Given Difference

def DiffPair(arr,target):
    paired = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]-arr[j])==target or (arr[i]-arr[j]) == -target:
                paired+=1
    return paired

A = [5, 10, 3, 2, 50, 80] #B = 78 Input 2: 
print(DiffPair(A,78))
A = [-10, 20]

print(DiffPair(A,30))
