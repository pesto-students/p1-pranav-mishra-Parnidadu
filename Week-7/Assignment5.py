def nextGreater(arr):
    for i in range(0, len(arr)):
        next = -1
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        print(str(arr[i]) + " next greater element is  " + str(next))

arr1 = [1, 3, 2, 4]
arr2 = [1,2,3,4,5,6]
nextGreater(arr1)
print('-'*50)
nextGreater(arr2)
