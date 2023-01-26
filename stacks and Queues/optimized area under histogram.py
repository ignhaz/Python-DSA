def area(arr):
    n = len(arr)
    s = []
    lc, rc = [-1], [n]
    
    # to get previous smaller element index.
    s.append(0)
    for i in range(1,n):
        while len(s)!=0 and arr[s[-1]] >= arr[i]:
            s.pop()
        if len(s)==0:
            lc.append(-1)
        else:
            lc.append(s[-1])
        s.append(i)
    
    #empty the stack.
    while (len(s)>0):
        s.pop()
    
    #to get next smaller elements index.
    s.append(n-1)
    i = n - 2
    while i>=0:
        while len(s) != 0 and arr[s[-1]] >= arr[i]:
            s.pop()
        if len(s) == 0:
            rc.append(n)
        else:
            rc.append(s[-1])
        s.append(i)
        i -= 1

    rc = rc[::-1]

    res = 0
    for i in range(0,n):
        area = arr[i]
        area = area + (i-lc[i]-1)*arr[i]
        area = area + (rc[i]-i-1)*arr[i]
        res = max(res,area)
    
    return res
    

arr = [11,2,5,4,1,7,6]
print(area(arr))