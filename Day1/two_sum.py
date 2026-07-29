def two_sum(arr , target):
    seen = {}
    for index , value in enumerate(arr):
        second_ele = target - value
        if second_ele in seen:
            return [index , seen[second_ele]]
        else :
            seen[value] = index
print(two_sum([2,7,11,15] , 9))