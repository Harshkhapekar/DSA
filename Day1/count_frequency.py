def frequency(arr):
    seen = {}
    count = 1

    for ele in arr:
        
        if ele  not in seen:
            seen[ele] = count
        else :
            seen[ele] += 1
    return seen

print(frequency([1,2,2,3,4,2,1,5]))