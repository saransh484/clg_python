# Function to do insertion sort
def insertionSort(arr):

        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):

            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j] :
                arr[j+1] =  arr[j]
                j -= 1
            arr[j+1] = key

arr = [100,50,6,8,10]
insertionSort(arr)
lst = [] #empty list to store sorted elements
print("Sorted array is : ")
for i in range(len(arr)):
    lst.append(arr[i])
print(lst)
