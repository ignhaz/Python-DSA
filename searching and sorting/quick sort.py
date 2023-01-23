def part(arr,low,high):
    swap_index = low - 1
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] < pivot:
            swap_index += 1
            arr[j], arr[swap_index] = arr[swap_index], arr[j]
            
    arr[swap_index+1], arr[high] = arr[high], arr[swap_index+1]

    return swap_index+1


def quick_sort(arr,low,high):
    if low < high:
        partition = part(arr,low,high)

        quick_sort(arr,partition+1,high)
        quick_sort(arr,low,partition-1)


arr = [70,90,10,30,50,20,60]
n = len(arr)

quick_sort(arr,0,n-1)

print(arr)