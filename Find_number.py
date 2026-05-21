lst = [1,3,5,6]  # find the number and return index , if not pr4sent return the index where it should be prsent
target = 4
left = 0
right = len(lst) -1 

while left <= right:
    mid = left + (right-left)//2
    if lst[mid] < target:
        left = mid +1
    elif lst[mid] > target:
        right = mid - 1
    else :
        print(mid)
        break;
else :
    print(f"The Target should be present at index {left}")     

    