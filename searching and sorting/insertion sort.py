def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp

arr = [8,6,4,20,24,2,10,12]
insertion_sort(arr)
print('Final sorted array: ',arr)