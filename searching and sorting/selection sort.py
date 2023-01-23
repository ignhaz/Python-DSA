def selection_sort(arr):
    for i in range(0,len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [10,1,4,1,5,7,12,3]
selection_sort(arr)
print(arr)