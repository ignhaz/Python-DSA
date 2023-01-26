def opre_smaller(arr):
    n = len(arr)
    s = []
    print('-',end=' ')
    s.append(arr[0])

    for i in range(1,n):
        while(len(s)!=0 and arr[i]<=s[-1]):
            s.pop()
        if len(s) == 0:
            print('-',end=' ')
        else:
            print(s[-1],end=' ')
        s.append(arr[i])

arr = [11,3,4,4,1,5,7]
opre_smaller(arr)