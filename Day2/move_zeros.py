def movezeros(arr):
    start = 0
    next = 1
    while next < len(arr):
        if arr[start] == 0 and arr[next] !=0:
            arr[start] , arr[next] = arr[next] , arr[start];
            start+=1
            next+=1
        elif  arr[start] == 0 and arr[next] ==0:
            next +=1
        else :
            start+=1
            next+=1
    return arr
print(movezeros([0, 1, 0, 3, 12]))