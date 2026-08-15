def duplicates(arr):
    seen = set()
    for ele in arr:
        if ele  in seen:
            return True
        else :
            seen.add(ele)
    return False
print(duplicates([1,2,3,4,1]))