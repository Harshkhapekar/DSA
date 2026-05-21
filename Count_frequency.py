""" HASHMAPS """

nums = [1,2,2,3,1,4,2] # count frequency of each numbers 
frequency = {}
count = 1
for num in nums:
    if num not in frequency:
        frequency[num] = count
    else :
        current_count = frequency[num]
        frequency[num] = current_count+1
print(frequency)


