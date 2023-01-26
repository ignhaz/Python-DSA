
# time complexity : O(n^2)
def stockspan(arr):
    for i in range(len(arr)):
        span = 1
        j = i - 1
        while j >=0  and arr[j] <= arr[i]:
            span += 1
            j = j - 1
        print(span,end=' ')

# time complexity: O(n)
# Optimized using stack concept.
def ostockspan(arr):
    n = len(arr)
    s = []
    s.append(0)
    print(1,end=' ')

    for i in range(1,n):
        while len(s) != 0 and arr[s[-1]] <= arr[i]:
            s.pop()
        if len(s) == 0:
            print(i+1,end=' ')
        else:
            print(i-s[-1],end=' ')
        s.append(i)




arr = [15,10,8,9,12,17]
ostockspan(arr)