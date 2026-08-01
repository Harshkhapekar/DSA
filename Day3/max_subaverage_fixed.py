def average(arr , k):
    window_size = arr[:k] 
    max_average = sum(window_size) / len(window_size)
    current_avg = max_average
    for index in range(k , len(arr)):
        current_avg = (current_avg *k - arr[index-k] + arr[index])/k
        max_average = max(max_average , current_avg)
    return max_average

print(average([1,12,-5,-6,50,3] , 4))