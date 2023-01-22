#Binary search works only when the array is sorted.

def binary_search(arr,L,R,k):
    if L <= R:
        M = L + (R - L) // 2
        if arr[M] == k:
            return M
        elif arr[M] < k:
            return binary_search(arr,M+1,R,k)
        else:
            return binary_search(arr,L,M-1,k)
    else:
        return -1

arr = [3,5,7,9,12,15,16,18,19,22]
L = 0
R = len(arr)-1
k = int(input('enter the element to be searched: '))

result = binary_search(arr,L,R,k)

if result == -1:
    print('Entered element NOT found')
else:
    print(f'Entered element found at INDEX {result}')