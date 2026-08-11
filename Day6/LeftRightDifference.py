from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = 0
        left_arr = []
        right_arr = []
        for ele in nums:
            left_arr.append(left_sum)
            left_sum+=ele
        for ele in nums[::-1]:
            right_arr.append(right_sum)
            right_sum+=ele
        return [abs(x-y) for x,y in zip(left_arr ,right_arr[::-1])]