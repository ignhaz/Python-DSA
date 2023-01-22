def linear_search(arr,k):
    l = len(arr)
    for i in range(0,l):
        if arr[i] == k:
            return i
        if i == l-1:
            return -1
        

arr = [1,2,3,4,5,6,7,8,9]
k = int(input('enter the element to be searched: '))

if linear_search(arr,k) == -1:
    print('Entered element not found')
else:
    print(f'Entered element found at index {linear_search(arr,k)}')