from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sum = 0
        for ele in nums:
            sum = sum+ele
            result.append(sum)
        return result