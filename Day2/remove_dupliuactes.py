def duplicates(arr):
    start = 0 
    next =  1
    count = 1
    while next < len(arr):
        if arr[start] == arr[next]:
            next +=1
        else :
            count+=1
            start += 1
            arr[start] = arr[next]
            next+=1
    return count
print(duplicates([1, 1, 2, 2, 3, 4, 4]))