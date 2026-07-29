def non_repeating(arr):
    seen = {}

    for ele in arr:
        if ele not in seen:
            seen[ele] = 1
        else :
            seen[ele] +=1
    for ele in arr:
        if seen[ele] == 1:
            return ele
    return -1
print(non_repeating([4, 5, 1, 2, 0, 4])) 