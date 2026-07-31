def sorted_squares(arr):
    result = []
    start = 0
    end = len(arr) - 1
    while start <= end:
        if arr[start]**2 < arr[end]**2:
            result.append(arr[end]**2)
            end-=1
        elif arr[start]**2 > arr[end]**2:
            result.append(arr[start]**2)
            start+=1
        else :
            result.append(arr[start]**2)
            start +=1
            end-=1
    return result[::-1]
print(sorted_squares([-4,-1,0,3,10]))
