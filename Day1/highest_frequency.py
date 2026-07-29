def highest_frequency(arr):
    seen = {}
    count = 1
    result = []
    for ele in arr:
        
        if ele  not in seen:
            seen[ele] = count
        else :
            seen[ele] += 1
    max_value = max(seen.values())
    for key , value in seen.items():
        if max_value == value:
            result.append(key)
    return min(result)

print(highest_frequency([2,2,3,4,1,2,1,1,5]))    