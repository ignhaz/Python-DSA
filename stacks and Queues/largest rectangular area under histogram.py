
#naive approach.
#time complexity: O(n^2)

def area(arr):
    ans = 0
    for i in range(len(arr)):

        count = 1
        l = i - 1 #for left side.
        r = i + 1 #for right side.

        while l >= 0:
            if arr[l] >= arr[i]:
                count += 1
                l -= 1
            else:
                break

        while r <= len(arr)-1:
            if arr[r] >= arr[i]:
                count += 1
                r += 1
            else:
                break
        
        ans = max(ans, count*arr[i])
    return ans

arr = [11,3,4,4,1,5,7]
print(area(arr))