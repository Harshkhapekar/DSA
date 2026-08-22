class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float("inf")

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                current_len = right - left + 1
                min_len = min(min_len, current_len)

                current_sum -= nums[left]
                left += 1

        if min_len == float("inf"):
            return 0

        return min_len