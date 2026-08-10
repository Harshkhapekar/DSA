from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt_sum = 0
        alt = [alt_sum]
        for ele in gain:
            alt_sum += ele
            alt.append(alt_sum)
        return max(alt)