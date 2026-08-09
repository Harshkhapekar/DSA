from typing import List
def maximumWealth( accounts: List[List[int]]) -> int:
        max_wealth = 0
        for wealth in accounts:
            current_wealth = sum(wealth)
            max_wealth = max(current_wealth , max_wealth)
        return max_wealth