def consecutives(arr , k):
    count = 0
    result = []
    max_len = 0
    left = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            count+=1
            result.append(arr[right])
        else :
            result.append(arr[right])
        if count <= k:
            max_len = max(max_len , len(result))

            

    return result

        
    
print(consecutives([1,1,1,0,0,0,1,1,1,1,0] , 2))
    