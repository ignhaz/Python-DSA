#arr=[0,1,2,4,5,6,7] -------> arr=[4,5,6,7,0,1,2]
# search for element k in the rotated array.

def rotated_search(arr,target):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l+r) // 2
        if arr[m] == target:
            return m
        else:
            # if element in left sorted array.
            if arr[m] >= arr[l]: #to check if mid is in left sorted part.
                if arr[m] < target or arr[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if arr[m] > target or arr[r] < target:
                    r = m - 1
                else:
                    l = m + 1
    return -1


arr = [3,4,5,6,7,8,9,1,2]
k = 8
print(rotated_search(arr,k))