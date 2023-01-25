def bs(arr,n,x):
    l, r = 0, n-1
    i = -1
    while l <= r:
        m = (l+r)//2
        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            r = m - 1
        else:
            i = m
            l = m + 1 # for last occurence
            # r = m - 1 for first occurence
    return i

            


arr = [1,2,3,5,5,5,5,5,123,125]
x = 5
res = bs(arr,len(arr),x)
print('last occurence at INDEX:',res)