def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        return -1
arr = ['t', 'u', 'm', 'o', 'r', 'i', 'a', 'l']
x = 't'
print("element found at index "+str(linearsearch(arr,x)))
