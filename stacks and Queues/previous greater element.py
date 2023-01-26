# Optimized algorithm
# Time complexity: O(n)
def opre_greater(arr):
    n = len(arr)
    s = []
    print('-',end=' ')
    s.append(arr[0])

    for i in range(1,n):
        while(len(s)!=0 and arr[i]>=s[-1]):
            s.pop()
        if len(s) == 0:
            print('-',end=' ')
        else:
            print(s[-1],end=' ')
        s.append(arr[i])


# Time complexity: O(n^2)
def pre_greater(arr):
    n = len(arr)
    print('-',end=' ')
    for i in range(1,n):
        flag = False
        j = i - 1
        while j>=0:
            if arr[j] > arr[i]:
                flag = True
                print(arr[j],end=' ')
                break
            else:
                j -= 1
        if flag == False:
            print('-',end=' ')

arr = [20,10,20,22,15,14,18,32,20,22,19]
pre_greater(arr)