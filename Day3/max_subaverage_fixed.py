class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[0:k])
        max_avg = current_sum / k
        for index in range(k , len(nums)):
            current_sum =  current_sum - nums[index-k] + nums[index]
            max_avg = max(max_avg , current_sum/k)
        return max_avg
