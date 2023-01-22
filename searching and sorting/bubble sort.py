def bubble_sort(arr,n):
    for i in range(n-1):
        swapped = False

        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break

    return arr

arr = [28,6,4,2,36,24]

print(bubble_sort(arr,len(arr)))